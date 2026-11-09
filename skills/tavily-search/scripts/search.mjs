// Compatibility wrapper: cron agents historically call search.mjs.
// Delegates to simple-search.mjs (key-pool + Bearer auth). Usage identical.
import { spawnSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const res = spawnSync(process.execPath, [join(here, 'simple-search.mjs'), ...args], { stdio: 'inherit' });
process.exit(res.status ?? 1);
