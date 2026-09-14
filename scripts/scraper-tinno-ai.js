const { chromium } = require('/root/.claude/skills/gstack/node_modules/playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
  });
  const page = await context.newPage();

  try {
    // BOSS直聘搜索天珑+AI
    await page.goto('https://www.zhipin.com/web/geek/job?query=天珑+AI&city=101280600', {
      waitUntil: 'networkidle',
      timeout: 30000
    });
    await page.waitForTimeout(3000);

    // 提取岗位列表
    const jobs = await page.evaluate(() => {
      const items = document.querySelectorAll('.job-card-wrapper, .job-card-left');
      const results = [];
      
      items.forEach(item => {
        try {
          const title = item.querySelector('.job-name')?.textContent?.trim() || '';
          const salary = item.querySelector('.salary')?.textContent?.trim() || '';
          const company = item.querySelector('.company-name a')?.textContent?.trim() || '';
          const tags = Array.from(item.querySelectorAll('.tag-list li')).map(t => t.textContent.trim());
          const area = item.querySelector('.job-area')?.textContent?.trim() || '';
          
          if (title && salary) {
            results.push({ title, salary, company, area, tags });
          }
        } catch(e) {}
      });
      return results;
    });

    console.log(JSON.stringify(jobs, null, 2));

    if (jobs.length === 0) {
      // 尝试截图看看页面状态
      console.log('=== NO_JOBS_FOUND ===');
      console.log('PAGE_TITLE:', await page.title());
      const bodyText = await page.evaluate(() => document.body?.innerText?.substring(0, 2000) || '');
      console.log('PAGE_TEXT:', bodyText);
    }
  } catch (e) {
    console.error('ERROR:', e.message);
  } finally {
    await browser.close();
  }
})();
