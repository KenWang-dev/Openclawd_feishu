const { chromium } = require('/root/.claude/skills/gstack/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  });
  const page = await context.newPage();

  // 尝试多个搜索
  const queries = [
    { name: '51job', url: 'https://search.51job.com/list/000000,000000,0000,00,9,99,%E5%A4%A9%E7%8F%91,2,1.html' },
    { name: 'zhipin-mobile', url: 'https://m.zhipin.com/job_detail/?query=天珑+AI&city=101280600' },
    { name: 'boss-company', url: 'https://www.zhipin.com/gongsi/a32ab7a7b2f5660503F429S-Ew~~.html' },
  ];

  for (const q of queries) {
    try {
      console.log(`\n=== ${q.name} ===`);
      await page.goto(q.url, { waitUntil: 'domcontentloaded', timeout: 20000 });
      await page.waitForTimeout(4000);
      const text = await page.evaluate(() => document.body?.innerText?.substring(0, 2000) || '');
      console.log(text);
    } catch(e) {
      console.log(`ERROR: ${e.message}`);
    }
  }

  await browser.close();
})();
