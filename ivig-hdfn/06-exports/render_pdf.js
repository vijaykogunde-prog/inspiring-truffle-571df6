const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage();
  const htmlPath = 'file://' + path.resolve(__dirname, 'infographic.html');
  await page.goto(htmlPath, { waitUntil: 'networkidle' });
  await page.pdf({
    path: path.resolve(__dirname, 'IVIG-HDFN-Evidence-Infographic.pdf'),
    format: 'A4',
    printBackground: true,
    margin: { top: '0mm', bottom: '0mm', left: '0mm', right: '0mm' },
  });
  await browser.close();
  console.log('PDF written');
})();
