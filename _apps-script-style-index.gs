/**
 * IFE 2026 — Style the "Index" tab of "2026 IFE summer program AI modules"
 * Applies the block-card PDF design: week color-coding, AI-module vs Journey-only
 * shading, AOT highlights, and expands Journey lesson codes to "code + Title".
 * Also (re)builds a "Legend & Key" tab decoding every code.
 *
 * HOW TO RUN
 *   1. Open the Google Sheet → Extensions → Apps Script.
 *   2. Delete any boilerplate, paste this whole file, Save.
 *   3. Select function  styleIndex  → Run. Approve the one-time permission.
 *   (Tip: File → Make a copy of the sheet first if you want a safety net.
 *    Either way, Sheets version history can undo this.)
 *
 * Safe to re-run: it always re-derives codes from the cell text, so titles
 * never double up.
 */

// ---- CONFIG -----------------------------------------------------------
var EXPAND_ALL_ROWS = true;   // false = only expand Journey titles for Week 1 rows
var COLORS = {
  header:    '#2A2830', headerText: '#FFFFFF',
  w1: '#FBEFC9',  // Week 1 — soft yellow   (ai is a mirror)
  w2: '#FBDAD9',  // Week 2 — soft coral    (ai is a sampler)
  w3: '#CFEDE3',  // Week 3 — soft teal     (ai is a tool)
  w4: '#E7DCF7',  // Week 4 — soft purple   (ai is a position)
  none: '#F0EFEC',     // no AI module (Journey-only / site visit / pitch)
  module: '#D8ECE8',   // ai Module cell when present
  aot: '#FCE8B3',      // AOT confirmed
  aotCand: '#FBF3D6',  // AOT candidate (pending D-Cal)
  band: '#FFFFFF', line: '#D8D5DC', muted: '#8A8892'
};
// Block number -> week color
function weekColorForBlock(n){
  if (n>=1 && n<=3) return COLORS.w1;
  if (n>=4 && n<=7) return COLORS.w2;
  if (n>=8 && n<=11) return COLORS.w3;
  if (n>=12 && n<=14) return COLORS.w4;
  return COLORS.none;
}

// ---- Journey lesson titles -------------------------------------------
var LESSON_TITLES = {
  '1.1':'Journey Platform Onboarding','1.2':'Onboarding Survey','1.3':'Onboarding Challenges',
  '1.4':'Orientation','1.5':'Entrepreneurial Mindset','1.6':'Entrepreneurial Problem Solving',
  '1.7':'Your Entrepreneurial Profile','1.9':'What Apps Do You Love?','1.10':'Your First MVP',
  '1.12':'Telling Fact from Fictions Online',
  '2.1':'Teams & Tracks','2.3':'Design Thinking','2.4':'Problem Statement','2.5':'Stakeholder Mapping',
  '2.6':'Who is your Customer?','2.7':'How Might We?','2.8':'Customer Discovery (Secondary Sources)',
  '2.9':'Customer Discovery (Primary Sources)','2.10':'Innovation Challenge',
  '3.9':'How to Find and Keep a Mentor','3.10':'How to Give and Receive Feedback',
  '4.2':'Fieldwork Preparation','4.3':'Empathy Research Challenge','4.4':'HTML Essentials',
  '4.6':'Introduction to Flask','4.7':'Introduction to APIs','4.8':'How to Use Artificial Intelligence in Your App',
  '5.1':'Empathy Mapping','5.4':'Traction (Customer Validation)','5.7':'Data Analysis and Data Visualization',
  '6.1':'Prototype','6.2':'The Lean Startup & MVPs','6.3':'Business Model Creation','6.4':'Testing',
  '7.1':'Revenue Model and Pricing for your Startup','7.2':'Financial Strategy & Projections',
  '7.3':'Entrepreneurial Fundraising','8.1':'Market & Competitive Analysis',
  '8.2':'The Entrepreneurial Pitch','8.3':'Final Personal Reflection Challenge','8.4':'The Final Pitch'
};

var SHEET_ID = '1yRyQ0prUEzAzXGa9CrdZbpCZmKWjhAqbL2LAVGa-EUU';  // works in a standalone OR bound project

function styleIndex(){
  // openById works in any project; getActiveSpreadsheet() only works if the script is bound to the sheet.
  var ss = SpreadsheetApp.openById(SHEET_ID);

  // ---- Find the Index sheet + header row (contains "Journey anchors") ----
  var sheet=null, headerRow=-1, cols={};
  var sheets = ss.getSheets();
  for (var s=0; s<sheets.length && !sheet; s++){
    var sh = sheets[s];
    var rng = sh.getRange(1, 1, Math.min(5, sh.getMaxRows()), Math.min(12, sh.getMaxColumns())).getValues();
    for (var r=0; r<rng.length; r++){
      var row = rng[r].map(function(v){return String(v).trim();});
      if (row.indexOf('Journey anchors')>=0 && row.indexOf('ai Module')>=0){
        sheet=sh; headerRow=r+1;
        row.forEach(function(h,i){ cols[h]=i+1; });
        break;
      }
    }
  }
  if (!sheet){ throw new Error('Could not find the Index tab (a row with "ai Module" + "Journey anchors").'); }

  var cDay = cols['Day'], cMod = cols['ai Module'], cJrny = cols['Journey anchors'], cAot = cols['AOT content utilized'];
  var lastCol = sheet.getLastColumn();
  var firstData = headerRow+1;
  // last data row = last row where Day cell is a number
  var maxRow = sheet.getLastRow();
  var lastData = headerRow;
  for (var rr=firstData; rr<=maxRow; rr++){
    var dv = String(sheet.getRange(rr, cDay).getValue()).trim();
    if (dv && !isNaN(Number(dv))) lastData = rr; else if (dv==='') break;
  }
  if (lastData < firstData){ throw new Error('No data rows found under the header.'); }
  var nRows = lastData - firstData + 1;

  // ---- Header styling ----
  var hdr = sheet.getRange(headerRow, 1, 1, lastCol);
  hdr.setBackground(COLORS.header).setFontColor(COLORS.headerText).setFontWeight('bold')
     .setHorizontalAlignment('center').setVerticalAlignment('middle').setWrap(true);
  sheet.setFrozenRows(headerRow);

  // ---- Per-row styling ----
  for (var i=0; i<nRows; i++){
    var row = firstData + i;
    var modVal = String(sheet.getRange(row, cMod).getValue()).trim();
    var m = modVal.match(/B(\d+)/);
    var blockN = m ? Number(m[1]) : 0;
    var wk = weekColorForBlock(blockN);

    // Day cell + ai Module cell carry the week color (ties module to its week)
    sheet.getRange(row, cDay).setBackground(wk).setFontWeight('bold').setHorizontalAlignment('center');
    if (modVal){
      sheet.getRange(row, cMod).setBackground(wk).setFontWeight('bold');
    } else {
      sheet.getRange(row, cMod).setBackground(COLORS.none).setFontColor(COLORS.muted).setValue('—').setHorizontalAlignment('center');
    }

    // AOT highlight
    if (cAot){
      var aotVal = String(sheet.getRange(row, cAot).getValue()).trim();
      if (aotVal){
        var cand = /candidate/i.test(aotVal);
        sheet.getRange(row, cAot).setBackground(cand ? COLORS.aotCand : COLORS.aot)
             .setFontStyle(cand ? 'italic' : 'normal').setWrap(true);
      }
    }

    // Expand Journey codes -> "code  Title"
    if (cJrny && (EXPAND_ALL_ROWS || blockN>=1 && blockN<=3 || i<4)){
      var raw = String(sheet.getRange(row, cJrny).getValue());
      var codes = raw.match(/\d+\.\d+/g);
      if (codes){
        var lines = codes.map(function(c){ return LESSON_TITLES[c] ? (c + '  ' + LESSON_TITLES[c]) : c; });
        sheet.getRange(row, cJrny).setValue(lines.join('\n')).setWrap(true).setVerticalAlignment('top');
      }
    }
  }

  // ---- Table cosmetics ----
  var body = sheet.getRange(headerRow, 1, nRows+1, lastCol);
  body.setBorder(true, true, true, true, true, true, COLORS.line, SpreadsheetApp.BorderStyle.SOLID);
  body.setVerticalAlignment('top');
  if (cJrny) sheet.setColumnWidth(cJrny, 300);
  if (cAot)  sheet.setColumnWidth(cAot, 260);
  if (cols['Theme']) sheet.setColumnWidth(cols['Theme'], 220);

  buildLegend(ss);
  SpreadsheetApp.getActiveSpreadsheet().toast('Index styled + Legend & Key built.', 'Done', 5);
}

// ---- Legend & Key tab -------------------------------------------------
function buildLegend(ss){
  var name = 'Legend & Key';
  var sh = ss.getSheetByName(name);
  if (sh) ss.deleteSheet(sh);
  sh = ss.insertSheet(name, 0);  // put it first so it reads "at the beginning"
  sh.setHiddenGridlines(true);

  var rows = [];
  rows.push(['IFE 2026 · AI Literacy Track — Legend & Journey Key','']);
  rows.push(['Companion layer to the day-by-day Index. AI modules support Journey; they do not replace it.','']);
  rows.push(['','']);
  rows.push(['COLOR CODING','']);
  rows.push(['Week 1 — ai is a mirror, not a mind (B1–B3)','']);
  rows.push(['Week 2 — ai is a sampler, not a source (B4–B7)','']);
  rows.push(['Week 3 — ai is a tool, not an agent (B8–B11)','']);
  rows.push(['Week 4 — ai is a position, not a destination (B12–B14)','']);
  rows.push(['No AI module (Journey-only / site visit / pitch)','']);
  rows.push(['AOT content placed','']);
  rows.push(['AOT candidate (pending D-Cal L#)','']);
  rows.push(['','']);
  rows.push(['JOURNEY LESSON KEY','']);
  rows.push(['Code','Lesson title']);
  var keys = Object.keys(LESSON_TITLES).sort(function(a,b){
    var pa=a.split('.').map(Number), pb=b.split('.').map(Number);
    return pa[0]-pb[0] || pa[1]-pb[1];
  });
  keys.forEach(function(c){ rows.push([c, LESSON_TITLES[c]]); });

  sh.getRange(1,1,rows.length,2).setValues(rows);
  sh.getRange(1,1).setFontSize(15).setFontWeight('bold');
  sh.getRange(2,1).setFontColor(COLORS.muted);
  sh.getRange(4,1).setFontWeight('bold');
  sh.getRange(13,1).setFontWeight('bold');
  sh.getRange(14,1,1,2).setFontWeight('bold').setBackground(COLORS.header).setFontColor('#FFFFFF');

  // swatches on the color-coding rows
  var swatch = {5:COLORS.w1,6:COLORS.w2,7:COLORS.w3,8:COLORS.w4,9:COLORS.none,10:COLORS.aot,11:COLORS.aotCand};
  for (var r in swatch){ sh.getRange(Number(r),2).setBackground(swatch[r]); }

  sh.setColumnWidth(1, 360);
  sh.setColumnWidth(2, 320);
  sh.getRange(15,1,keys.length,1).setHorizontalAlignment('left').setFontWeight('bold');
}
