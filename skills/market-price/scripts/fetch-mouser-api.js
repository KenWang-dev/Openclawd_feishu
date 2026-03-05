// Mouser API - 正确的集成实现
const https = require('https');
const fs = require('fs');
const path = require('path');

// 从 .env 加载 API Key
function loadApiKey() {
  // 优先使用环境变量
  if (process.env.MOUSER_API_KEY) {
    return process.env.MOUSER_API_KEY;
  }
  
  // 其次从 .env 文件读取
  const envPath = path.join(__dirname, '.env');
  if (fs.existsSync(envPath)) {
    const envContent = fs.readFileSync(envPath, 'utf8');
    const match = envContent.match(/MOUSER_API_KEY=(.+)/);
    if (match) return match[1].trim();
  }
  
  throw new Error('❌ 未配置 MOUSER_API_KEY，请创建 .env 文件或设置环境变量');
}

const API_KEY = loadApiKey();

// 按 Part Number 搜索（推荐）
function searchByPartNumber(partNumbers) {
  return new Promise((resolve, reject) => {
    // 支持单个或多个料号（用 | 分隔）
    const searchPartNumber = Array.isArray(partNumbers)
      ? partNumbers.join('|')
      : partNumbers;

    const postData = JSON.stringify({
      SearchByPartRequest: {
        mouserPartNumber: searchPartNumber,
        partSearchOptions: 'Exact'
      }
    });

    const options = {
      hostname: 'api.mouser.com',
      port: 443,
      path: `/api/v1/search/partnumber?apiKey=${API_KEY}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = https.request(options, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const result = JSON.parse(data);

          if (result.SearchResults && result.SearchResults.Parts) {
            resolve({
              success: true,
              parts: result.SearchResults.Parts,
              errors: result.Errors
            });
          } else if (result.Errors) {
            reject({
              success: false,
              errors: result.Errors
            });
          } else {
            reject({
              success: false,
              message: 'Unknown response format',
              data: result
            });
          }
        } catch (error) {
          reject({
            success: false,
            error: error.message,
            raw: data
          });
        }
      });
    });

    req.on('error', (error) => {
      reject({
        success: false,
        error: error.message
      });
    });

    req.setTimeout(10000, () => {
      req.destroy();
      reject({
        success: false,
        error: 'Request timeout'
      });
    });

    req.write(postData);
    req.end();
  });
}

// 按 Keyword 搜索
function searchByKeyword(keyword, options = {}) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      SearchByKeywordRequest: {
        keyword: keyword,
        records: options.records || 10,
        startingRecord: options.startingRecord || 0,
        searchOptions: options.searchOptions || 'None',
        searchWithYourSignUpLanguage: options.searchWithYourSignUpLanguage || 'false'
      }
    });

    const requestOptions = {
      hostname: 'api.mouser.com',
      port: 443,
      path: `/api/v1/search/keyword?apiKey=${API_KEY}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = https.request(requestOptions, (res) => {
      let data = '';

      res.on('data', (chunk) => {
        data += chunk;
      });

      res.on('end', () => {
        try {
          const result = JSON.parse(data);

          if (result.SearchResults && result.SearchResults.Parts) {
            resolve({
              success: true,
              parts: result.SearchResults.Parts,
              errors: result.Errors
            });
          } else if (result.Errors) {
            reject({
              success: false,
              errors: result.Errors
            });
          } else {
            reject({
              success: false,
              message: 'Unknown response format',
              data: result
            });
          }
        } catch (error) {
          reject({
            success: false,
            error: error.message,
            raw: data
          });
        }
      });
    });

    req.on('error', (error) => {
      reject({
        success: false,
        error: error.message
      });
    });

    req.write(postData);
    req.end();
  });
}

// 解析 Mouser 返回的数据为统一格式
function parseMouserPart(mouserPart) {
  // 提取价格（取最后一个价格断点 = 最高阶梯的批量价格）
  let price = null;
  let priceWithTax = null; // 含税价格
  let taxRate = 0.13; // 默认 13% 税率（中国）
  let priceBreak = null; // 记录使用的价格阶梯
  
  if (mouserPart.PriceBreaks && mouserPart.PriceBreaks.length > 0) {
    // 取最后一个价格阶梯（最高批量价）
    priceBreak = mouserPart.PriceBreaks[mouserPart.PriceBreaks.length - 1];
    
    const priceStr = priceBreak.Price;
    // 移除货币符号和逗号
    const cleanPrice = priceStr.replace(/[^\d.]/g, '');
    price = parseFloat(cleanPrice);
    // 计算含税价格
    priceWithTax = price * (1 + taxRate);
  }

  // 解析库存
  let stock = 0;
  if (mouserPart.Availability) {
    // 库存字符串格式："145 in stock" 或 "0"
    const match = mouserPart.Availability.match(/(\d+)/);
    if (match) {
      stock = parseInt(match[1]);
    }
  }

  return {
    partNumber: mouserPart.MouserPartNumber,
    manufacturer: mouserPart.Manufacturer,
    manufacturerPartNumber: mouserPart.ManufacturerPartNumber,
    description: mouserPart.Description,
    price: price, // 基础价格（不含税，最高阶梯批量价）
    priceWithTax: priceWithTax, // 含税价格（13%，最高阶梯批量价）
    priceBreakQuantity: priceBreak ? priceBreak.Quantity : null, // 价格阶梯数量
    taxRate: taxRate,
    stock: stock,
    availability: mouserPart.Availability,
    leadTime: mouserPart.LeadTime,
    lifecycleStatus: mouserPart.LifecycleStatus,
    dataSheetUrl: mouserPart.DataSheetUrl,
    productUrl: mouserPart.ProductDetailUrl,
    imageUrl: mouserPart.ImagePath,
    category: mouserPart.Category,
    minOrderQty: mouserPart.Min,
    multiple: mouserPart.Mult,
    rohsStatus: mouserPart.ROHSStatus,
    priceBreaks: mouserPart.PriceBreaks,
    raw: mouserPart
  };
}

// 测试函数
async function test() {
  console.log('========================================');
  console.log('🧪 Mouser API 测试（正确格式）');
  console.log('========================================\n');

  const testParts = [
    'STM32F103C8T6',
    'ESP32-S3-WROOM-1',
    'CH340G'
  ];

  // 测试 1：单个查询
  console.log('--- 测试 1: 单个料号查询 ---');
  try {
    const result = await searchByPartNumber('STM32F103C8T6');
    if (result.success) {
      console.log(`✅ 找到 ${result.parts.length} 个结果`);
      if (result.parts.length > 0) {
        const parsed = parseMouserPart(result.parts[0]);
        console.log(`   料号: ${parsed.partNumber}`);
        console.log(`   制造商: ${parsed.manufacturer}`);
        console.log(`   描述: ${parsed.description}`);
        console.log(`   价格: $${parsed.price}`);
        console.log(`   库存: ${parsed.stock} (${parsed.availability})`);
        console.log(`   交期: ${parsed.leadTime}`);
      }
    }
  } catch (error) {
    console.error('❌ 失败:', error.error || error.errors || error.message);
  }

  // 延迟
  await new Promise(resolve => setTimeout(resolve, 2000));

  // 测试 2：批量查询
  console.log('\n--- 测试 2: 批量料号查询 ---');
  try {
    const result = await searchByPartNumber(testParts);
    if (result.success) {
      console.log(`✅ 找到 ${result.parts.length} 个结果`);
      result.parts.forEach(part => {
        const parsed = parseMouserPart(part);
        console.log(`\n   ${parsed.partNumber}:`);
        console.log(`   - 制造商: ${parsed.manufacturer}`);
        console.log(`   - 价格: $${parsed.price}`);
        console.log(`   - 库存: ${parsed.stock}`);
      });
    }
  } catch (error) {
    console.error('❌ 失败:', error.error || error.errors || error.message);
  }

  console.log('\n========================================');
  console.log('✅ 测试完成');
  console.log('========================================');
}

// 导出模块
module.exports = {
  searchByPartNumber,
  searchByKeyword,
  parseMouserPart
};

// 如果直接运行，执行测试
if (require.main === module) {
  test().catch(console.error);
}
