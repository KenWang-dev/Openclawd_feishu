// 简化版：使用 JSON 文件存储，无需 SQLite 依赖
const fs = require('fs');
const path = require('path');

const dataDir = path.join(__dirname, '../data');
const componentsFile = path.join(dataDir, 'components.json');
const historyDir = path.join(dataDir, 'history');

// 确保目录存在
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}
if (!fs.existsSync(historyDir)) {
  fs.mkdirSync(historyDir, { recursive: true });
}

// 初始化元器件数据
function initComponents() {
  if (!fs.existsSync(componentsFile)) {
    const components = [
      { 
        id: 1,
        part_number: 'STM32F103C8T6', 
        description: 'STM32 32位微控制器', 
        category: '芯片',
        min_stock: 10,
        price_threshold: 0.05,
        enabled: true 
      },
      { 
        id: 2,
        part_number: 'ESP32-S3-WROOM-1', 
        description: 'ESP32-S3 WiFi模块', 
        category: '模块',
        min_stock: 10,
        price_threshold: 0.05,
        enabled: true 
      },
      { 
        id: 3,
        part_number: 'CH340G', 
        description: 'USB转串口芯片', 
        category: '芯片',
        min_stock: 50,
        price_threshold: 0.05,
        enabled: true 
      }
    ];
    
    fs.writeFileSync(componentsFile, JSON.stringify(components, null, 2));
    console.log('✅ 初始化元器件数据');
    return components;
  }
  
  return JSON.parse(fs.readFileSync(componentsFile, 'utf8'));
}

// 保存价格历史
function savePriceHistory(partNumber, data) {
  const today = new Date().toISOString().split('T')[0];
  const historyFile = path.join(historyDir, `${partNumber}.json`);
  
  let history = [];
  if (fs.existsSync(historyFile)) {
    history = JSON.parse(fs.readFileSync(historyFile, 'utf8'));
  }
  
  history.push({
    ...data,
    captured_at: new Date().toISOString()
  });
  
  // 只保留最近100条记录
  if (history.length > 100) {
    history = history.slice(-100);
  }
  
  fs.writeFileSync(historyFile, JSON.stringify(history, null, 2));
}

// 获取上次价格
function getLastPrice(partNumber) {
  const historyFile = path.join(historyDir, `${partNumber}.json`);
  
  if (!fs.existsSync(historyFile)) {
    return null;
  }
  
  const history = JSON.parse(fs.readFileSync(historyFile, 'utf8'));
  if (history.length === 0) {
    return null;
  }
  
  return history[history.length - 1];
}

// 导出汇总数据到 CSV
function exportSummaryCSV() {
  const summaryFile = path.join(dataDir, 'price-summary.csv');
  const components = initComponents();
  
  // CSV 表头
  let csv = '时间,物料类型,MPN,品牌,含税单价(¥),批量,库存,供应商,备注\n';
  
  // 遍历所有物料
  for (const comp of components) {
    const historyFile = path.join(historyDir, `${comp.part_number}.json`);
    
    if (!fs.existsSync(historyFile)) continue;
    
    const history = JSON.parse(fs.readFileSync(historyFile, 'utf8'));
    
    // 只取最新的记录
    if (history.length > 0) {
      const latest = history[history.length - 1];
      const time = latest.captured_at ? latest.captured_at.split('T')[0] : '';
      const category = comp.category || '';
      const mpn = comp.part_number;
      const price = latest.price || latest.priceWithTax || '';
      const brand = latest.manufacturer || latest.brand || '';
      const quantity = latest.priceBreakQuantity || '';
      const stock = latest.stock || '';
      const supplier = latest.supplier || '';
      const remark = latest.leadTime ? `交期:${latest.leadTime}` : '';
      
      csv += `${time},${category},${mpn},${brand},${price},${quantity},${stock},${supplier},${remark}\n`;
    }
  }
  
  fs.writeFileSync(summaryFile, '\ufeff' + csv); // BOM for Excel
  return summaryFile;
}

// 导出模块
module.exports = {
  initComponents,
  savePriceHistory,
  getLastPrice,
  exportSummaryCSV,
  dataDir,
  historyDir
};
