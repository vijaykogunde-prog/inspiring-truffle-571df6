const fs = require("fs");

function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
function p(text) { return `<p>${esc(text)}</p>\n`; }
function h1(text) { return `<h1>${esc(text)}</h1>\n`; }
function h2(text) { return `<h2>${esc(text)}</h2>\n`; }
function li(text) { return `<li>${esc(text)}</li>\n`; }
function fig(file, widthPct, caption) {
  return `<div class="figwrap"><img src="patient-figures/${file}" style="width:${widthPct}%;" />${caption ? `<p class="figcap">${esc(caption)}</p>` : ""}</div>\n`;
}
function table(headers, rows, widths) {
  const thead = `<tr>${headers.map((h, i) => `<th style="width:${widths ? widths[i] : ""}">${esc(h)}</th>`).join("")}</tr>`;
  const tbody = rows.map((r) => `<tr>${r.map((c) => `<td>${esc(c)}</td>`).join("")}</tr>`).join("\n");
  return `<table>\n${thead}\n${tbody}\n</table>\n`;
}

let body = "";

// ---------------------------------------------------------------------
// Cover
// ---------------------------------------------------------------------
body += `
<div class="cover">
  <div class="cover-kicker">INFORMATION FOR YOU AND YOUR FAMILY</div>
  <h1 class="cover-title">Steroid Injections Before an Early Birth</h1>
  <p class="cover-sub">A plain-English guide to why these injections are offered, what to expect, and honest answers to the questions parents ask most</p>
</div>
`;

// ---------------------------------------------------------------------
// Intro
// ---------------------------------------------------------------------
body += h1("What are these injections for?");
body += p("If your doctors or midwives think your baby might be born early, they may offer you an injection of a steroid medicine. This is a different kind of steroid to the ones used for muscle-building or for allergies. It is a medicine that has been used safely in pregnancy for over fifty years.");
body += p("The steroid crosses to your baby and helps their lungs get ready to breathe air. It also lowers the chance of some other problems that can affect babies born too soon. Two medicines can be used, dexamethasone or betamethasone, and both work in a very similar way. Your team may give you either one, and this is not a sign that anything has gone wrong or that one is being chosen over the other for any special reason.");

body += fig("p4_infographic.png", 96);

// ---------------------------------------------------------------------
// Flowchart
// ---------------------------------------------------------------------
body += h1("What happens, step by step");
body += p("The injection is usually given as two doses, about 24 hours apart (sometimes as four smaller doses, 12 hours apart, which works just as well). It is given into your arm, thigh, or bottom, in the same way as many other injections.");
body += fig("p1_journey.png", 92);

// ---------------------------------------------------------------------
// Table: the two medicines
// ---------------------------------------------------------------------
body += h1("The two medicines, side by side");
body += table(
  ["", "Dexamethasone", "Betamethasone"],
  [
    ["Usual pattern", "4 smaller injections, 12 hours apart", "2 injections, 24 hours apart"],
    ["Total medicine given", "About the same overall dose", "About the same overall dose"],
    ["How well it works", "No meaningful difference found between the two in the largest study comparing them directly", "No meaningful difference found between the two in the largest study comparing them directly"],
  ],
  ["30%", "35%", "35%"]
);
body += p("A note on dosing schedules: if you were told your injections would be 12 hours apart rather than 24, this is not unusual or a mistake. It is one of the standard ways this medicine is given around the world.");

// ---------------------------------------------------------------------
// Bar chart: benefits
// ---------------------------------------------------------------------
body += h1("What difference does it make?");
body += p("Researchers have followed thousands of babies whose mothers had this injection before an early birth, compared with babies whose mothers did not. Here is what a large review of 27 studies, involving more than 11 000 babies, found.");
body += fig("p3_bar.png", 92);
body += p("These numbers are averaged across babies born at different stages of pregnancy. As a general rule, the benefit is bigger the earlier your baby is due, and smaller if your baby is close to full term.");

// ---------------------------------------------------------------------
// Partial course
// ---------------------------------------------------------------------
body += h1("What if I only have one injection?");
body += p("Sometimes there is only time for one injection before your baby arrives. This is still much better than no injection at all. In one large study, a single injection given less than 24 hours before birth cut the extra risk linked to being born early by around half, compared with having no injection. Your team will always try to give the first dose as early as possible, even if they think there may not be time for a second.");
body += p("If your baby arrives very soon after your injection, perhaps even within an hour, there is no evidence this causes any harm, and it may still help. Your medical team will not delay the injection just because your baby's arrival might be very close.");

// ---------------------------------------------------------------------
// Pie chart: late preterm
// ---------------------------------------------------------------------
body += h1("If your baby is due between 34 and 37 weeks");
body += p("Babies born a little early, between 34 and 37 weeks, are much less likely to have serious problems than babies born very early. Even so, a large study looked at whether the injection still helps at this stage.");
body += fig("p2_pie.png", 88);
body += p("The injection did lower the chance of needing breathing support. It also made low blood sugar in the first day or two after birth somewhat more common, though this is usually mild and settles on its own within a day. Your baby's blood sugar will be checked as a routine part of their care if you have this injection close to a late-preterm birth.");

// ---------------------------------------------------------------------
// Mixed / incomplete courses
// ---------------------------------------------------------------------
body += h1("What if I had a mix of both medicines, or an incomplete course?");
body += p("Occasionally, because of how quickly things happen, you might end up with one dose of one medicine and one dose of the other, rather than two doses of the same one. This is not a mistake, and it does not mean your baby missed out on the benefit. Your baby will still have received real, meaningful medicine. Because this exact combination has not been specifically studied, your team cannot say for certain it worked exactly as well as two doses of a single medicine, so it will be noted in your records and your baby may be monitored a little more closely, in the same way as if you had an incomplete course.");
body += p("The same applies if you only had a single dose for any reason. It is documented clearly, and it is not treated as a problem, just as useful information for your baby's team.");

// ---------------------------------------------------------------------
// Term exposure - honest section
// ---------------------------------------------------------------------
body += h1("\"If my baby doesn't end up arriving early after all, could the injection still affect them?\"");
body += p("This is one of the questions parents ask most, and it deserves an honest answer rather than a simple reassurance.");

body += table(
  ["What we know", "What we don't know"],
  [
    ["A very large study from Finland, following hundreds of thousands of children, found a somewhat higher rate of mental health or developmental diagnoses in children who had the injection before birth but were then born at full term.", "Whether the injection itself caused this, or whether it reflects the reason the injection was given in the first place (such as high blood pressure, a placenta problem, or another sign the pregnancy looked risky)."],
    ["When researchers compared brothers and sisters in the same family, who share genes and home environment, the difference became smaller, though it did not disappear completely.", "Exactly how much smaller effect, if any, remains once every other factor is accounted for."],
    ["A separate large study, from Taiwan, looked at the same question and found no difference at all in babies born at full term.", "Why the two studies point in different directions; this could reflect real differences between populations, or the limits of this kind of research."],
    ["For babies who are genuinely born early, and this is most babies who receive the injection, the evidence for benefit is strong and consistent, including in studies that followed people for over 30 years.", "There is no known reason to expect a different, unstudied risk for the small number of babies who go on to reach full term."],
  ],
  ["50%", "50%"]
);

body += p("A short answer you may hear from your team: \"The strongest evidence, including studies that followed people for over thirty years after this treatment, hasn't found a difference in thinking, memory, or mental health in adults who received it as unborn babies and were then born early, which is when this treatment is mainly used. There's a separate, harder question about babies who have the injection but then go on to be born at full term. Some large studies have found a small difference in that group, others have found none, and we cannot be sure whether any difference is caused by the injection itself or by whatever made the pregnancy look risky in the first place. We won't dismiss this question, and we won't overstate it either.\"");

// ---------------------------------------------------------------------
// Repeat courses
// ---------------------------------------------------------------------
body += h1("What if I need more than one course?");
body += p("If your pregnancy continues and you remain at high risk of an early birth more than a week after your first course, your team may talk to you about a second course. This can further reduce breathing problems for your baby. It also tends to make your baby slightly smaller at birth, by around 100 grams on average. The longest follow-up study of babies who had a repeat course, over 20 years, found this size difference did not affect their long-term health.");
body += p("The one situation where extra care is taken is if a repeat course is given and the pregnancy then continues all the way to full term. This is the group in which any downside from repeat dosing has shown up most clearly, which is why repeat courses are limited to specific situations, usually to a maximum of two in total.");

// ---------------------------------------------------------------------
// Questions table
// ---------------------------------------------------------------------
body += h1("Questions you might want to ask your team");
body += "<ul>" +
  li("Which medicine am I being given, and how many doses have I had so far?") +
  li("Given how soon I might deliver, is there still a benefit to having another dose?") +
  li("Is there anything about my situation, such as signs of infection, that changes the usual approach?") +
  li("What will you be watching for in my baby after birth because of this treatment?") +
  li("If I need a repeat course later in my pregnancy, what would that mean?") +
  "</ul>";

// ---------------------------------------------------------------------
// Sources
// ---------------------------------------------------------------------
body += h1("Where this information comes from");
body += p("This leaflet is based on a review of the major research studies and national guidelines on this treatment, including:");
body += "<ul>" +
  li("A Cochrane Review (2020), which combined the results of 27 studies from around the world, involving more than 11 000 babies.") +
  li("The ASTEROID trial (2019), the largest study directly comparing the two medicines.") +
  li("The ALPS trial (New England Journal of Medicine, 2016), the main study of this treatment in babies due between 34 and 37 weeks.") +
  li("Long-term follow-up studies, including one that followed people for over 30 years after they received this treatment before birth.") +
  li("National guidance from the Royal College of Obstetricians and Gynaecologists, NICE, and the World Health Organization.") +
  "</ul>";
body += p("This is general information to support a conversation with your own doctors and midwives, who know your individual circumstances. It is not a substitute for their advice.");

// ---------------------------------------------------------------------
// CSS + document
// ---------------------------------------------------------------------
const css = `
@page {
  size: A4;
  margin: 18mm 16mm 20mm 16mm;
  @bottom-center { content: counter(page); font-size: 8.5pt; color: #8AA; }
}
* { box-sizing: border-box; }
body { font-family: Calibri, "Liberation Sans", Arial, sans-serif; font-size: 11.3pt; line-height: 1.55; color: #1a2b2b; }
.cover { text-align: center; padding: 40pt 10pt 10pt 10pt; }
.cover-kicker { font-size: 10pt; font-weight: 700; letter-spacing: 2px; color: #C9791C; margin-bottom: 10pt; }
.cover-title { font-size: 27pt; color: #0F4C4C; margin: 0 0 12pt 0; line-height: 1.25; }
.cover-sub { font-size: 12.5pt; color: #3A5252; max-width: 480pt; margin: 0 auto; font-style: italic; }
h1 { font-size: 16pt; color: #0F4C4C; margin: 22pt 0 9pt 0; border-bottom: 1.6pt solid #1B7A72; padding-bottom: 4pt; }
h2 { font-size: 12.5pt; color: #1B7A72; margin: 12pt 0 6pt 0; }
p { margin: 0 0 10pt 0; text-align: justify; }
ul { padding-left: 20pt; margin: 0 0 12pt 0; }
li { margin-bottom: 7pt; }
.figwrap { text-align: center; margin: 10pt 0 14pt 0; page-break-inside: avoid; }
.figwrap img { max-width: 100%; }
.figcap { font-size: 9pt; color: #5B6B6B; text-align: center; margin-top: 4pt; }
table { width: 100%; border-collapse: collapse; margin: 8pt 0 14pt 0; font-size: 10.3pt; }
th { background: #1B7A72; color: white; text-align: left; padding: 7pt 9pt; font-weight: 600; }
td { padding: 7pt 9pt; border-bottom: 0.5pt solid #D9E7E5; vertical-align: top; text-align: left; }
tr:nth-child(even) td { background: #F2F9F8; }
.pagebreak { page-break-before: always; }
`;

const html = `<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Steroid Injections Before an Early Birth</title><style>${css}</style></head>
<body>${body}</body>
</html>`;

const outPath = "/home/user/inspiring-truffle-571df6/acs-evidence-synthesis/Patient_information_leaflet.html";
fs.writeFileSync(outPath, html);
console.log("Wrote", outPath);
