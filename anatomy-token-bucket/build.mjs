import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as k from "../../skills/anatomy/kit/iso-kit.mjs";
import { kitScript } from "../../skills/anatomy/scripts/inline-kit.mjs";

const HERE = dirname(fileURLToPath(import.meta.url));
const theme = process.argv.includes("--light") ? "light" : "dark";

// ---------------------------------------------------------------- truth
// Token bucket: refill rate r tokens/s drip from the feeder into the
// bucket (capacity b = 12). Each request takes exactly one token through
// the gate; an empty bucket closes the gate and the request is refused.
const CAP = 12;
const REFILL = 2.0; // tokens per second, default
const FLOOR = 26; // bucket floor top (z)
const COIN_H = 4.2;
const COIN_R = 27;
const RIM_Z = 92; // bucket rim

// ---------------------------------------------------------------- layout
const WIDTH = 720;
const HEIGHT = 450;

const PLATE = { x: -158, y: -84, w: 316, d: 148, r: 8 };
const PLATE_H = 12;
const FOOT_H = 5;

const BUCKET = { cx: -48, cy: 0, r: 34, wall: 5 };
const NOZZLE = [-48, 0, 146];
const POST = [-48, 44]; // feeder support post
const POST_TOP = 170;
const HOPPER = { cx: -48, cy: 0, r: 20, z: 154, h: 30 };

const CHUTE = { x: -20, y: -7, w: 56, d: 14, r: 1.5 };
const CHUTE_FLOOR_TOP = 28;
const GATE = { x: -17, y: -8.2, w: 9, d: 16.4, r: 1.5 };
const GATE_Z = 26;

const TRAY = { x: -124, y: -58, w: 34, d: 26, r: 3 }; // overflow tray
const OUT = { x: 50, y: 16, w: 34, d: 26, r: 3 }; // passed-request tray

const BTN = { x: 88, y: -8, w: 18, d: 16, r: 2 };
const BTN_CX = 97, BTN_CY = 0;
const LAMP = [124, -56];
const GAUGE = { x: -44, y: 40, w: 2.2, d: 8, r: 0.6, z0: 24, z1: 80 };

const P = k.fitProjection(
  [
    ...k.boxCorners(PLATE, -PLATE_H - FOOT_H, 0),
    [-48, 0, HOPPER.z + HOPPER.h + 6],
    [POST[0] + 4, POST[1] + 4, POST_TOP + 5],
    [LAMP[0] + 8, LAMP[1], 50],
    [OUT.x + OUT.w, OUT.y + OUT.d, 8],
  ],
  WIDTH,
  HEIGHT,
  { pad: 28, azimuth: 42 },
);

const at = (point) => k.iso(point, P);
const S = (paths, style) => k.solidSvg(paths, style);
const L = (d, style) => k.lineSvg(d, style);
const D = (points, style) => k.dotsSvg(points, style);
const seg = (a, b, style) => L(k.segment(a, b, P), style);
const byDepth = (points) => [...points].sort((a, b) => k.depthOf([a[0], a[1], 0], P) - k.depthOf([b[0], b[1], 0], P));

// half-annulus plan (for the cut-open bucket shell and its rim)
function halfAnnulus(cx, cy, ro, ri, a0, a1, steps = 24) {
  const out = [];
  for (let i = 0; i <= steps; i++) {
    const a = a0 + ((a1 - a0) * i) / steps;
    out.push([cx + ro * Math.cos(a), cy + ro * Math.sin(a)]);
  }
  for (let i = steps; i >= 0; i--) {
    const a = a0 + ((a1 - a0) * i) / steps;
    out.push([cx + ri * Math.cos(a), cy + ri * Math.sin(a)]);
  }
  return out;
}
const VIEW = Math.PI / 4; // viewer sits on the +x+y diagonal
const BACK_A0 = VIEW, BACK_A1 = VIEW + Math.PI;

// one token coin, shared by build and live (injected with toString)
function coinSvg(cx, cy, z, r, h) {
  return solidSvg(cylinder(cx, cy, r, z, h, P, 26, 0.5), { tone: "hi", crease: "lo" });
}

// ---------------------------------------------------------------- parts
function base() {
  const out = [`<path class="iso-halo" d="${k.haloOf(PLATE, -PLATE_H - FOOT_H, PLATE_H, P)}"/>`];
  for (const [x, y] of byDepth(k.corners(PLATE, 22))) {
    out.push(S(k.cylinder(x, y, 7, -PLATE_H - FOOT_H, 1.6, P, 28), { tone: "lo" }));
    out.push(S(k.cylinder(x, y, 5.4, -PLATE_H - FOOT_H + 1.6, FOOT_H - 1.6, P, 28), { tone: "mid" }));
  }
  out.push(S(k.slabOf(PLATE, -PLATE_H, PLATE_H, P, 8, 1.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(PLATE, 5), 0, P), { tone: "lo" }));
  const screws = k.corners(PLATE, 10);
  out.push(L(screws.map(([x, y]) => k.ring(x, y, 2.2, 0, P, 16)).join(""), { tone: "lo" }));
  out.push(D(screws.map(([x, y]) => at([x, y, 0])), { size: 0.5 }));

  // token-count ruler strip under the bucket, ticks = 1 token each
  const strip = { x: -96, y: 56, w: 128, d: 7, r: 1 };
  out.push(S(k.slabOf(strip, 0, 0.6, P, 3), { tone: "lo", crease: "none" }));
  const ticks = k.topTicks(strip.x + 5, strip.x + strip.w - 5, 128 / CAP, 3, strip.y + 0.8, 0.6, [2, 3.6], P);
  out.push(L(ticks.minor, { tone: "lo" }), L(ticks.major, { tone: "mid" }));
  out.push(D([at([strip.x + 2, strip.y + 3.5, 0.6]), at([strip.x + strip.w - 2, strip.y + 3.5, 0.6])], { size: 0.45 }));
  for (const n of [0, 6, 12]) {
    const x = strip.x + 5 + (n / CAP) * (strip.w - 10);
    out.push(k.faceTextSvg(k.topMatrix([x, strip.y + strip.d + 4], 0, P, "x"), String(n), { size: 2.6, tone: "lo", anchor: "middle" }));
  }
  out.push(k.faceTextSvg(k.topMatrix([strip.x + strip.w + 10, strip.y + 3.5], 0, P, "x"), "TOKENS", { size: 2.4, tone: "lo", anchor: "start" }));

  // engraved label plate
  const plate = { x: 56, y: 56, w: 54, d: 15, r: 2 };
  out.push(S(k.slabOf(plate, 0, 1.4, P, 3, 0.4), { tone: "lo" }));
  out.push(L(k.planOutline(k.insetPlan(plate, 2), 1.4, P, 3), { tone: "mid" }));
  out.push(k.faceTextSvg(k.topMatrix([plate.x + plate.w / 2, plate.y + plate.d / 2 + 1], 1.4, P, "x"), "RATE LIMITER", { size: 2.8, tone: "mid", anchor: "middle" }));
  return out.join("");
}

function pedestal() {
  const out = [];
  const { cx, cy } = BUCKET;
  out.push(S(k.cylinder(cx, cy, 16, 0, 2, P, 32), { tone: "mid" }));
  out.push(S(k.cylinder(cx, cy, 13, 2, FLOOR - 2 - 4, P, 32), { tone: "mid", crease: "none" }));
  out.push(L([8, 12].map((z) => k.sideArc(cx, cy, 13, z, P, 20)).join(""), { tone: "faint" }));
  // bucket floor disc
  out.push(S(k.cylinder(cx, cy, BUCKET.r - BUCKET.wall, FLOOR - 4, 4, P, 40), { tone: "lo" }));
  out.push(L(k.ring(cx, cy, BUCKET.r - BUCKET.wall - 2, FLOOR, P, 40), { tone: "faint" }));
  return out.join("");
}

function bucketShell() {
  const out = [];
  const { cx, cy, r, wall } = BUCKET;
  const shell = k.extrude(halfAnnulus(cx, cy, r, r - wall, BACK_A0, BACK_A1, 28), FLOOR, RIM_Z - FLOOR, P, { convex: false });
  out.push(S(shell, { tone: "mid", crease: "faint" }));
  // seams on the curved wall
  for (const a of [Math.PI * 0.75, Math.PI]) {
    const px = cx + r * Math.cos(a), py = cy + r * Math.sin(a);
    out.push(seg([px, py, FLOOR], [px, py, RIM_Z], { tone: "faint" }));
  }
  // handle ears
  for (const s of [-1, 1]) {
    const a = Math.PI + s * 0.9;
    const px = cx + (r + 1) * Math.cos(a), py = cy + (r + 1) * Math.sin(a);
    out.push(S(k.cylinder(px, py, 3, RIM_Z - 8, 4, P, 20), { tone: "mid" }));
    out.push(D([at([px, py, RIM_Z - 4])], { size: 0.45 }));
  }
  return out.join("");
}

function bucketRim() {
  const out = [];
  const { cx, cy, r, wall } = BUCKET;
  const rim = k.extrude(halfAnnulus(cx, cy, r, r - wall, 0, Math.PI * 2, 36), RIM_Z, 5, P, { convex: false, bevel: 0.6 });
  out.push(S(rim, { tone: "mid" }));
  out.push(L(k.ring(cx, cy, r - wall / 2, RIM_Z + 5, P, 36), { tone: "faint" }));
  return out.join("");
}

function feeder() {
  const out = [];
  // support post + clamp + arm
  out.push(S(k.cylinder(POST[0], POST[1], 4, 0, 4, P, 24), { tone: "mid" }));
  out.push(S(k.cylinder(POST[0], POST[1], 3, 4, POST_TOP - 4, P, 24), { tone: "mid", crease: "none" }));
  out.push(L([40, 90, 140].map((z) => k.sideArc(POST[0], POST[1], 3, z, P, 16)).join(""), { tone: "faint" }));
  out.push(S(k.slabOf({ x: POST[0] - 5.5, y: POST[1] - 5.5, w: 11, d: 11, r: 2 }, POST_TOP, 7, P, 3, 0.5), { tone: "mid" }));
  out.push(S(k.cylinder(POST[0], POST[1] + 7, 2.4, POST_TOP, 5, P, 18), { tone: "mid" }));
  out.push(L(k.knurl(POST[0], POST[1] + 7, 2.4, POST_TOP, POST_TOP + 5, 16, P), { tone: "lo" }));
  out.push(S(k.slabOf({ x: POST[0] - 4, y: 6, w: 8, d: 40, r: 2 }, POST_TOP + 7, 4, P, 3, 0.5), { tone: "mid" }));
  out.push(D([at([POST[0], 10, POST_TOP + 11]), at([POST[0], 42, POST_TOP + 11])], { size: 0.45 }));

  // feeder drum the tokens drip from
  const { cx, cy, r, z, h } = HOPPER;
  out.push(S(k.cylinder(cx, cy, r, z, h, P, 40, 0.8), { tone: "mid" }));
  out.push(S(k.cylinder(cx, cy, r + 1.6, z + 4, 3, P, 40), { tone: "mid" }));
  out.push(S(k.cylinder(cx, cy, r + 1.6, z + h - 8, 3, P, 40), { tone: "mid" }));
  out.push(L(k.ring(cx, cy, r, z + h, P, 40), { tone: "lo" }));
  out.push(L(k.ring(cx, cy, r - 3, z + h, P, 40), { tone: "lo" }));
  out.push(S(k.cylinder(cx, cy, r - 3, z + h, 1.2, P, 40), { tone: "lo", crease: "none" }));
  // metering nozzle + collar + rate knob
  out.push(S(k.cylinder(cx, cy, 5, NOZZLE[2], z - NOZZLE[2], P, 24), { tone: "mid", crease: "none" }));
  out.push(S(k.cylinder(cx, cy, 8, NOZZLE[2] + 4, 4, P, 24), { tone: "mid" }));
  out.push(L(k.knurl(cx + 7, cy, 3.4, NOZZLE[2] + 2, NOZZLE[2] + 8, 20, P), { tone: "lo" }));
  out.push(S(k.cylinder(cx + 7, cy, 3.4, NOZZLE[2] + 1.6, 6.4, P, 20), { tone: "mid" }));
  out.push(D([at([cx + 7, cy, NOZZLE[2] + 8])], { size: 0.5, tone: "hi" }));
  return out.join("");
}

function gauge() {
  const out = [];
  out.push(S(k.slabOf(GAUGE, GAUGE.z0, GAUGE.z1 - GAUGE.z0, P, 2, 0.4), { tone: "lo" }));
  const fx = GAUGE.x + GAUGE.w + 0.3;
  for (let i = 0; i <= CAP; i++) {
    const z = FLOOR + i * COIN_H;
    const len = i % 3 === 0 ? 4.6 : 2.6;
    out.push(seg([fx, GAUGE.y + 0.6, z], [fx, GAUGE.y + 0.6 + len, z], { tone: i % 3 === 0 ? "mid" : "lo" }));
    if (i % 6 === 0) {
      out.push(k.faceTextSvg(k.sideMatrix([fx + 0.6, GAUGE.y + 6.4, z - 2.2], z, P, "y"), String(i), { size: 2, tone: "lo", anchor: "start" }));
    }
  }
  return out.join("");
}

function gateAndChute() {
  const out = [];
  // chute: floor + back wall + end wall, open front (cutaway)
  out.push(S(k.slabOf(CHUTE, 24, CHUTE_FLOOR_TOP - 24, P, 3, 0.5), { tone: "mid" }));
  out.push(S(k.slabOf({ x: CHUTE.x, y: CHUTE.y, w: CHUTE.w, d: 3.5, r: 1 }, CHUTE_FLOOR_TOP, 12, P, 3, 0.5), { tone: "mid" }));
  out.push(S(k.slabOf({ x: CHUTE.x + CHUTE.w - 4, y: CHUTE.y, w: 4, d: CHUTE.d, r: 1 }, CHUTE_FLOOR_TOP, 12, P, 3, 0.5), { tone: "mid" }));
  out.push(D([at([CHUTE.x + 6, CHUTE.y + 1.8, CHUTE_FLOOR_TOP]), at([CHUTE.x + CHUTE.w - 10, CHUTE.y + 1.8, CHUTE_FLOOR_TOP])], { size: 0.4, tone: "lo" }));
  // valve body the gate slides in
  out.push(S(k.slabOf({ x: GATE.x - 2.5, y: GATE.y - 1.5, w: GATE.w + 5, d: GATE.d + 3, r: 2 }, 20, 22, P, 3, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan({ x: GATE.x - 2.5, y: GATE.y - 1.5, w: GATE.w + 5, d: GATE.d + 3, r: 2 }, 1.5), 42, P, 3), { tone: "faint" }));
  // gate: live group, slides up to open
  const gate = [];
  gate.push(S(k.slabOf(GATE, GATE_Z, 15, P, 2, 0.5), { tone: "hi", crease: "lo" }));
  gate.push(L(k.planOutline(k.insetPlan(GATE, 1.6), GATE_Z + 15, P, 2), { tone: "lo" }));
  gate.push(S(k.cylinder(GATE.x + GATE.w / 2, 0, 3, GATE_Z + 15, 4, P, 20), { tone: "hi" }));
  gate.push(L(k.knurl(GATE.x + GATE.w / 2, 0, 3, GATE_Z + 15, GATE_Z + 19, 18, P), { tone: "lo" }));
  out.push(`<g data-part="gate" transform="${k.translateAlong(P, [0, 0, 0])}">${gate.join("")}</g>`);
  // spring that closes the gate
  out.push(S(k.slabOf({ x: GATE.x - 4.5, y: 7.5, w: 3, d: 4, r: 1 }, 20, 3, P, 2), { tone: "mid", crease: "none" }));
  for (const z of [23.5, 25.5, 27.5]) out.push(L(k.ring(GATE.x - 3, 9.5, 1.8, z, P, 16), { tone: "lo" }));
  return out.join("");
}

function trays() {
  const out = [];
  for (const [plan, label] of [[TRAY, "OVERFLOW"], [OUT, "PASSED"]]) {
    out.push(S(k.slabOf(plan, 2, 6, P, 3, 0.6), { tone: "mid" }));
    out.push(L(k.planOutline(k.insetPlan(plan, 3), 4, P, 3), { tone: "faint" }));
    out.push(D(k.corners(plan, 4).map(([x, y]) => at([x, y, 8])), { size: 0.4, tone: "lo" }));
    out.push(k.faceTextSvg(k.topMatrix([plan.x + plan.w / 2, plan.y + plan.d + 5], 0, P, "x"), label, { size: 2.2, tone: "lo", anchor: "middle" }));
  }
  return out.join("");
}

function buttonAndLamp() {
  const out = [];
  // request button on a spring
  out.push(S(k.slabOf(BTN, 0, 10, P, 3, 0.6), { tone: "mid" }));
  out.push(L(k.planOutline(k.insetPlan(BTN, 2.5), 10, P, 3), { tone: "faint" }));
  for (const z of [11, 12.5, 14, 15.5]) out.push(L(k.ring(BTN_CX, BTN_CY, 5, z, P, 20), { tone: "lo" }));
  const cap = [];
  cap.push(S(k.cylinder(BTN_CX, BTN_CY, 7, 16, 6, P, 28, 0.6), { tone: "hi", crease: "lo" }));
  cap.push(L(k.knurl(BTN_CX, BTN_CY, 7, 17, 21, 30, P), { tone: "lo" }));
  cap.push(D([at([BTN_CX, BTN_CY, 22])], { size: 0.5, tone: "hi" }));
  out.push(`<g data-part="cap" transform="${k.translateAlong(P, [0, 0, 0])}">${cap.join("")}</g>`);
  // signal wire from button to the gate body
  out.push(k.wireSvg(at([BTN.x + BTN.w - 3, BTN.y + 2, 9]), at([GATE.x - 2.5, -4, 34]), { via: [at([60, -26, 46])], tone: "lo", size: 1 }));
  // status lamp on a post
  out.push(S(k.cylinder(LAMP[0], LAMP[1], 3.5, 0, 4, P, 20), { tone: "mid" }));
  out.push(S(k.cylinder(LAMP[0], LAMP[1], 2.6, 4, 38, P, 20), { tone: "mid", crease: "none" }));
  out.push(L(k.sideArc(LAMP[0], LAMP[1], 2.6, 24, P, 12), { tone: "faint" }));
  out.push(S(k.cylinder(LAMP[0], LAMP[1], 7.5, 42, 8, P, 28, 0.6), { tone: "mid" }));
  out.push(L(k.ring(LAMP[0], LAMP[1], 6, 50, P, 28), { tone: "lo" }));
  const [lx, ly] = at([LAMP[0], LAMP[1], 50.5]);
  const lr = 4.6 * P.scale * Math.sqrt(1.6) * 0.92;
  out.push(`<circle data-part="lamp" cx="${lx.toFixed(1)}" cy="${ly.toFixed(1)}" r="${lr.toFixed(1)}" fill="var(--lamp, transparent)" stroke="var(--lamp-ring)" stroke-width="0.8"/>`);
  out.push(k.wireSvg(at([LAMP[0] - 3, LAMP[1] + 3, 8]), at([BTN.x + 3, BTN.y + 3, 8]), { via: [at([112, -30, 14])], tone: "lo", size: 1 }));
  return out.join("");
}

const svg = k.figureSvg({
  width: WIDTH,
  height: HEIGHT,
  label:
    "A token bucket drawn as a bench machine: a feeder drum drips token coins into a cut-open bucket at a fixed rate; each press of the request button opens a gate and lets exactly one coin run down the chute into the passed tray; an empty bucket leaves the gate shut and lights the red lamp, while tokens above capacity spill into the overflow tray.",
  body: [
    base(),
    trays(),
    pedestal(),
    bucketShell(),
    `<g data-part="coins"></g>`,
    `<g data-part="drips"></g>`,
    bucketRim(),
    feeder(),
    gauge(),
    `<line data-part="pointer" class="iso-line" data-tone="lit" data-free="start" x1="0" y1="0" x2="0" y2="0" style="stroke-width:1.1"/>`,
    gateAndChute(),
    buttonAndLamp(),
    `<g data-part="exit"></g>`,
  ],
});

// ---------------------------------------------------------------- live
const lampPass = theme === "light" ? "#1f9d55" : "#57c983";
const lampBlock = theme === "light" ? "#c92a2a" : "#e05a5a";
const live = `
const P = ${JSON.stringify(P)};
const CAP = ${CAP}, REFILL = ${REFILL}, FLOOR = ${FLOOR}, COIN_H = ${COIN_H}, COIN_R = ${COIN_R};
const NOZZLE = ${JSON.stringify(NOZZLE)};
const POST = ${JSON.stringify(POST)};
const GATE = ${JSON.stringify(GATE)};
const CHUTE_FLOOR = ${CHUTE_FLOOR_TOP};
const OUT = ${JSON.stringify(OUT)};
const TRAY = ${JSON.stringify(TRAY)};
const BTN_CX = ${BTN_CX}, BTN_CY = ${BTN_CY};
const LAMP = ${JSON.stringify(LAMP)};
const LAMP_PASS = ${JSON.stringify(lampPass)};
const LAMP_BLOCK = ${JSON.stringify(lampBlock)};
const GAUGE = ${JSON.stringify(GAUGE)};
const coinSvg = ${coinSvg.toString()};

const stage = document.querySelector(".iso-stage");
const svg = stage.querySelector("svg");
const coins = svg.querySelector('[data-part="coins"]');
const drips = svg.querySelector('[data-part="drips"]');
const exitG = svg.querySelector('[data-part="exit"]');
const gate = svg.querySelector('[data-part="gate"]');
const cap = svg.querySelector('[data-part="cap"]');
const lamp = svg.querySelector('[data-part="lamp"]');
const pointer = svg.querySelector('[data-part="pointer"]');
const readout = document.querySelector("[data-readout]");
const still = matchMedia("(prefers-reduced-motion: reduce)");
document.documentElement.style.setProperty("--lamp-ring", getComputedStyle(document.querySelector(".iso-figure")).color);

// ---- model: one token bucket
const model = {
  tokens: 7, rate: REFILL, dripAcc: 0,
  drips: [], exit: null, gateUp: 0, gateTarget: 0, press: 0,
  lamp: 0, lampKind: "pass", last: "idle", idleAt: 0, auto: true,
};

function drawCoins() {
  const full = Math.floor(model.tokens);
  const frac = model.tokens - full;
  let html = "";
  for (let i = 0; i < full; i++) html += coinSvg(-48, 0, FLOOR + i * COIN_H, COIN_R, COIN_H - 0.7);
  if (full < CAP && frac > 0.02) html += coinSvg(-48, 0, FLOOR + full * COIN_H, COIN_R, 1.4 + frac * (COIN_H - 2.1));
  if (coins.__html !== html) { coins.innerHTML = html; coins.__html = html; }
}
function drawStatic() {
  drawCoins();
  const gz = FLOOR + Math.min(model.tokens, CAP) * COIN_H;
  const a = segment([GAUGE.x + GAUGE.w + 0.6, GAUGE.y + 0.2, gz], [GAUGE.x + GAUGE.w + 0.6, GAUGE.y + GAUGE.d, gz], P);
  pointer.setAttribute("d", a);
  const color = model.lampKind === "block" && model.lamp > 0.02 ? LAMP_BLOCK : LAMP_PASS;
  lamp.setAttribute("fill", color);
  lamp.setAttribute("fill-opacity", (0.15 + 0.85 * model.lamp).toFixed(3));
  const text = "tokens " + model.tokens.toFixed(1) + " / " + CAP + " · drip " + model.rate.toFixed(1) + "/s · last: " + model.last;
  if (readout.textContent !== text) readout.textContent = text;
  stage.setAttribute("aria-valuenow", String(Math.round(model.tokens)));
  stage.setAttribute("aria-valuetext", text);
}
function draw() {
  drawStatic();
  gate.setAttribute("transform", translateAlong(P, [0, 0, model.gateUp]));
  cap.setAttribute("transform", translateAlong(P, [0, 0, -model.press * 3.4]));
  // drips in flight
  let dh = "";
  for (const d of model.drips) {
    const [x, y] = d.kind === "overflow" ? dripOverflow(d.t) : [NOZZLE[0], NOZZLE[1]];
    dh += coinSvg(x, y, d.z, 4.5, 3.4);
  }
  if (drips.__html !== dh) { drips.innerHTML = dh; drips.__html = dh; }
  // the coin running the gauntlet
  let eh = "";
  if (model.exit) {
    const e = model.exit, t = e.t;
    let x, z;
    if (t < 0.45) { x = -13 + (t / 0.45) * 47; z = CHUTE_FLOOR + 1.6; }
    else {
      const u = (t - 0.45) / 0.55;
      x = 34 + u * (OUT.x + OUT.w / 2 - 34);
      z = CHUTE_FLOOR + 1.6 + (9 - CHUTE_FLOOR - 1.6) * u * u;
    }
    eh += coinSvg(x, 0, z, 5, 3);
  }
  if (exitG.__html !== eh) { exitG.innerHTML = eh; exitG.__html = eh; }
}
function dripOverflow(t) {
  const u = Math.max(0, (t - 0.55) / 0.45);
  return [NOZZLE[0] + (TRAY.x + TRAY.w / 2 - NOZZLE[0]) * u, NOZZLE[1] + (TRAY.y + TRAY.d / 2 - NOZZLE[1]) * u];
}

function request() {
  model.auto = false; model.idleAt = 0;
  if (model.tokens >= 1 && !model.exit) {
    model.tokens -= 1;
    model.exit = { t: 0 };
    model.gateTarget = 13;
    model.lamp = 1; model.lampKind = "pass";
    model.last = "passed";
  } else if (model.tokens < 1) {
    model.lamp = 1; model.lampKind = "block";
    model.last = "blocked · bucket empty";
    model.press = 1;
  }
}
function steer(delta) {
  model.rate = Math.min(6, Math.max(0.5, Math.round((model.rate + delta) * 2) / 2));
  model.last = "drip rate set";
}

function tick(now) {
  const dt = last ? Math.min((now - last) / 1000, 1 / 30) : 1 / 60;
  last = now;
  const m = model;
  // refill: drips spawn at the nozzle at rate/s
  m.dripAcc += m.rate * dt;
  if (m.dripAcc >= 1 && m.drips.length < 3) {
    m.dripAcc -= 1;
    m.drips.push({ z: NOZZLE[2] - 2, t: 0, kind: m.tokens >= CAP ? "overflow" : "fill" });
  }
  for (const d of m.drips) {
    d.t += dt / (d.kind === "overflow" ? 1.5 : 0.9);
    const land = d.kind === "overflow" ? 11 : FLOOR;
    d.z = NOZZLE[2] - 2 - d.t * (NOZZLE[2] - 2 - land);
    if (d.t >= 1) { if (d.kind === "fill" && m.tokens < CAP) m.tokens = Math.min(CAP, m.tokens + 1); d.done = true; }
  }
  m.drips = m.drips.filter((d) => !d.done);
  // exit coin and gate
  if (m.exit) {
    m.exit.t += dt / 0.95;
    if (m.exit.t > 0.35) m.gateTarget = 0;
    if (m.exit.t >= 1) m.exit = null;
  }
  m.gateUp += (m.gateTarget - m.gateUp) * (1 - Math.exp(-dt / 0.09));
  if (m.exit) m.press += (1 - m.press) * (1 - Math.exp(-dt / 0.08));
  else m.press = Math.max(0, m.press - dt / 0.35);
  m.lamp = Math.max(0, m.lamp - dt / 1.4);
  // idle tour: unattended requests every ~2 s
  m.idleAt += dt;
  if (m.auto && m.idleAt > 2 && !m.exit) { m.idleAt = 0; request(); m.auto = true; }
  draw();
  frame = visible && !still.matches ? requestAnimationFrame(tick) : 0;
}
let frame = 0, last = 0, visible = false;
const run = () => { if (!frame && visible && !still.matches) { last = 0; frame = requestAnimationFrame(tick); } };
new IntersectionObserver((entries) => { visible = entries[entries.length - 1].isIntersecting; if (visible) run(); }, { rootMargin: "120px 0px" }).observe(stage);
stage.addEventListener("pointerdown", (e) => { e.preventDefault(); request(); if (visible) { last = 0; if (!frame) frame = requestAnimationFrame(tick); } });
stage.addEventListener("keydown", (e) => {
  if (e.key === " " || e.key === "Enter") { e.preventDefault(); request(); }
  if (e.key === "ArrowUp" || e.key === "ArrowRight") { e.preventDefault(); steer(+0.5); }
  if (e.key === "ArrowDown" || e.key === "ArrowLeft") { e.preventDefault(); steer(-0.5); }
  if (visible) { last = 0; if (!frame) frame = requestAnimationFrame(tick); }
});
drawStatic();
`;

const body = k.plateHtml({
  fig: "Fig 1",
  title: "Token bucket rate limiter",
  hint: "Click or press Space to send a request · ↑ ↓ refill rate",
  readout: `tokens 7.0 / ${CAP} · drip ${REFILL.toFixed(1)}/s · last: idle`,
  keys: [
    { mark: "lit", label: "Gate and pointer: one coin per accepted request" },
    { mark: "raised", label: "Bucket holds up to 12 token coins; overflow spills to its tray" },
  ],
  caption:
    "A token bucket as a bench machine. The feeder drips one token coin at a time into the bucket — the refill rate r. Each press of the request button lifts the gate and lets exactly one coin run down the chute: the request passes. When the bucket has drained, the gate stays shut, the lamp turns red and the request is refused; when the bucket is full, fresh tokens spill into the overflow tray instead of piling up.",
  body: `<div class="iso-stage" tabindex="0" role="slider" aria-label="Token bucket: Space sends a request, arrow keys change the refill rate" aria-valuemin="0" aria-valuemax="${CAP}" aria-valuenow="7">${svg}</div>`,
});

writeFileSync(join(HERE, theme === "light" ? "token-bucket-light.html" : "token-bucket.html"), k.pageHtml({ title: "Token bucket rate limiter", theme, body, script: kitScript() + live }));
console.log("wrote", theme === "light" ? "token-bucket-light.html" : "token-bucket.html");
