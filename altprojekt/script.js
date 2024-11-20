document.getElementById('calculateButton').addEventListener('click', function() {
  const kredit = parseFloat(document.getElementById('kredit').value);
  const zahlung = parseFloat(document.getElementById('zahlung').value);
  const zinse = parseFloat(document.getElementById('zinse').value);

  let kreditRest = kredit;
  let gesamtZinsen = 0;
  let monate = 0;

  while (kreditRest > zahlung) {
    const zinsen = (kreditRest * zinse / 100) / 12;
    gesamtZinsen += zinsen;
    kreditRest += zinsen - zahlung;
    monate++;
  }

  const ergebnisDiv = document.getElementById('result');
  ergebnisDiv.innerHTML = `
    <p>Sie müssen ${monate} Monaten weiter bezahlen</p>
    <p>Ihre letzte Zahlung wird ${kreditRest.toFixed(2)} € betragen</p>
    <p>Es wird ${parseFloat(monate / 12).toFixed(1)} Jahren dauern</p>
    <p>Sie bezahlen insgesamt ${gesamtZinsen.toFixed(2)} € Zinsen</p>
  `;
});
