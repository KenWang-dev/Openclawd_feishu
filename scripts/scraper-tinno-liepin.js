const { chromium } = require('/root/.claude/skills/gstack/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  });
  const page = await context.newPage();

  try {
    // 猎聘搜索天珑 AI
    await page.goto('https://www.liepin.com/zhaopin/?key=天珑+AI&currentPage=0', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });
    await page.waitForTimeout(5000);

    const bodyText = await page.evaluate(() => document.body?.innerText?.substring(0, 3000) || '');
    console.log('=== PAGE TEXT ===');
    console.log(bodyText);

    // 尝试提取岗位
    const jobs = await page.evaluate(() => {
      const items = document.querySelectorAll('[class*="job"], [class*="position"], .job-info, .sojob-item');
      const results = [];
      items.forEach(item => {
        const title = item.querySelector('[class*="title"], [class*="name"], h3, h4, a')?.textContent?.trim() || '';
        const salary = item.querySelector('[class*="salary"], [class*="text-warning"]')?.textContent?.trim() || '';
        const company = item.querySelector('[class*="company"]')?.textContent?.trim() || '';
        if (title) results.push({ title, salary, company });
      });
      return results;
    });

    if (jobs.length > 0) {
      console.log('\n=== JOBS ===');
      console.log(JSON.stringify(jobs, null, 2));
    }

    // 截图看看
    await page.screenshot({ path: '/root/.openclaw/workspace/scripts/liepin-screenshot.png' });
    console.log('\nScreenshot saved.');
    
  } catch (e) {
    console.error('ERROR:', e.message);
  } finally {
    await browser.close();
  }
})();
