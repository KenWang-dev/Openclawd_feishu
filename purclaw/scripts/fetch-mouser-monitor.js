// Mouser 价格监控 - 生产版本
const { initComponents, savePriceHistory, getLastPrice, exportSummaryCSV, dataDir } = require('./data-store');
const { searchByPartNumber, parseMouserPart } = require('./fetch-mouser-api');

async function monitorMouser() {
  console.log('========================================');
  console.log('📊 Mouser 价格监控 - ' + new Date().toLocaleString('zh-CN', {timeZone: 'Asia/Shanghai'}));
  console.log('========================================\n');

  try {
    const components = initComponents();
    console.log(`📦 监控物料数: ${components.length}\n`);

    const results = [];
    const partNumbers = components.map(c => c.part_number);

    // 批量查询所有料号
    console.log('🔍 批量查询 Mouser...');
    const mouserResult = await searchByPartNumber(partNumbers);

    if (!mouserResult.success) {
      console.error('❌ Mouser API 查询失败:', mouserResult.errors);
      return;
    }

    console.log(`✅ 找到 ${mouserResult.parts.length} 个结果\n`);

    // 创建查找表
    const partsMap = {};
    for (const part of mouserResult.parts) {
      const parsed = parseMouserPart(part);
      partsMap[parsed.manufacturerPartNumber] = parsed;
      // 也用 Mouser 料号做索引
      partsMap[parsed.partNumber] = parsed;
    }

    // 处理每个元器件
    for (const comp of components) {
      if (!comp.enabled) continue;

      console.log(`--- ${comp.part_number} ---`);

      // 查找对应的 Mouser 数据
      const mouserData =
        partsMap[comp.part_number] ||
        Object.values(partsMap).find(p => p.manufacturerPartNumber === comp.part_number);

      if (mouserData) {
        console.log(`✅ 找到: ${mouserData.manufacturer} ${mouserData.partNumber}`);
        console.log(`   批量价格 (${mouserData.priceBreakQuantity}+片): ¥${mouserData.price.toFixed(2)} (不含税)`);
        console.log(`   含税价格 (${mouserData.priceBreakQuantity}+片): ¥${mouserData.priceWithTax ? mouserData.priceWithTax.toFixed(2) : 'N/A'} (含13%税)`);
        console.log(`   库存: ${mouserData.stock} (${mouserData.availability})`);
        console.log(`   交期: ${mouserData.leadTime}`);

        // 获取上次价格
        const lastPrice = getLastPrice(comp.part_number);

        // 保存历史记录（使用含税价格作为主要价格）
        savePriceHistory(comp.part_number, {
          supplier: 'Mouser',
          price: mouserData.priceWithTax, // 含税价格（主要使用）
          priceBase: mouserData.price, // 基础价格（不含税）
          priceBreakQuantity: mouserData.priceBreakQuantity, // 价格阶梯数量
          taxRate: mouserData.taxRate,
          stock: mouserData.stock,
          availability: mouserData.availability,
          leadTime: mouserData.leadTime,
          mouserPartNumber: mouserData.partNumber,
          manufacturer: mouserData.manufacturer,
          description: mouserData.description
        });

        // 检测价格变动（使用含税价格）
        let change = null;
        if (lastPrice && lastPrice.price && mouserData.priceWithTax) {
          const changePercent = ((mouserData.priceWithTax - lastPrice.price) / lastPrice.price) * 100;
          change = {
            oldPrice: lastPrice.price,
            newPrice: mouserData.priceWithTax,
            percent: changePercent.toFixed(2)
          };

          if (Math.abs(changePercent) >= comp.price_threshold * 100) {
            console.log(`📈 价格变动: ${changePercent >= 0 ? '↑' : '↓'} ${change.percent}%`);
          }
        }

        // 检测缺货
        if (mouserData.stock === 0) {
          console.log(`🔴 缺货警告`);
        }

        // 检测库存低位
        if (mouserData.stock > 0 && mouserData.stock < comp.min_stock) {
          console.log(`⚠️  库存低位: ${mouserData.stock} < ${comp.min_stock}`);
        }

        results.push({
          component: comp,
          mouser: mouserData,
          change
        });
      } else {
        console.log(`⚠️  未找到: ${comp.part_number}`);
        results.push({
          component: comp,
          mouser: null
        });
      }

      console.log('');
    }

    // 汇总报告
    console.log('========================================');
    console.log('📊 监控摘要');
    console.log('========================================');
    console.log(`总计: ${components.length} 个`);
    console.log(`成功: ${results.filter(r => r.mouser).length} 个`);
    console.log(`未找到: ${results.filter(r => !r.mouser).length} 个`);

    const priceChanges = results.filter(r => r.change && Math.abs(parseFloat(r.change.percent)) >= r.component.price_threshold * 100);
    if (priceChanges.length > 0) {
      console.log(`\n⚠️  价格变动: ${priceChanges.length} 个`);
      priceChanges.forEach(r => {
        console.log(`   ${r.component.part_number}: ${r.change.newPrice >= r.change.oldPrice ? '↑' : '↓'} ${r.change.percent}%`);
      });
    }

    const outOfStock = results.filter(r => r.mouser && r.mouser.stock === 0);
    if (outOfStock.length > 0) {
      console.log(`\n🔴 缺货: ${outOfStock.length} 个`);
      outOfStock.forEach(r => {
        console.log(`   ${r.component.part_number}`);
      });
    }

    const lowStock = results.filter(r => r.mouser && r.mouser.stock > 0 && r.mouser.stock < r.component.min_stock);
    if (lowStock.length > 0) {
      console.log(`\n⚠️  库存低位: ${lowStock.length} 个`);
      lowStock.forEach(r => {
        console.log(`   ${r.component.part_number}: ${r.mouser.stock} < ${r.component.min_stock}`);
      });
    }

    console.log('\n✅ 监控完成（Mouser API）');
    
    // 导出汇总 CSV
    const csvFile = exportSummaryCSV();
    console.log(`📄 汇总已保存: ${csvFile}`);
    
    console.log('\n💡 下次运行: 4 小时后');

  } catch (error) {
    console.error('❌ 执行失败:', error.message);
    process.exit(1);
  }
}

// 导出模块
module.exports = { monitorMouser };

// 如果直接运行，执行监控
if (require.main === module) {
  monitorMouser().catch(console.error);
}
