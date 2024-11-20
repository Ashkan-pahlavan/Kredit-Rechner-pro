const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function kreditRechner() {
  try {
    console.log("      ***   Willkommen beim Kreditrechner-Programm :)   *** ");
    rl.question("Geben Sie hier ein, wie viel Kredit Sie benötigen: ", (kreditInput) => {
      const kredit = parseFloat(kreditInput);

      rl.question("Wie viel können Sie monatlich bezahlen: ", (zahlungInput) => {
        const zahlung = parseFloat(zahlungInput);

        rl.question("Geben Sie den jährlichen Zinsen Ihrer Bank ein: ", (zinseInput) => {
          const zinse = parseFloat(zinseInput);

          const zz = [];
          const list = [];
          const zmoatlich = [];

          while (true) {
            const zinsen = (kredit * zinse) / 100 / 12;

            if (zahlung > zinsen) {
              if (kredit > zahlung) {
                const nettoZ = zahlung - zinsen;
                const restschuld = kredit - nettoZ;
                kredit = restschuld;
                zz.push(parseFloat(zinsen.toFixed(1)));
                list.push(parseFloat(restschuld.toFixed(1)));
                zmoatlich.push(parseFloat(nettoZ.toFixed(1)));
              } else {
                const restzahlung = kredit;
                const zzz = zz.reduce((acc, val) => acc + val, 0);
                const z = list.length;
                console.log(`Sie sollen ${z + 1} Monaten weiter bezahlen`);
                console.log(` * Ihre letzte Zahlung wird ${restzahlung.toFixed(2)} €`);
                console.log(`Es wird ${parseFloat(z / 12).toFixed(1)} Jahren`);
                console.log(`Sie bezahlen insgesamt ${zzz.toFixed()} € Zinsen`);
                rl.question("Wollen Sie wissen, wie viel Sie monatlich an Zinsen zahlen? : j/n ", (userInput1) => {
                  if (userInput1.toLowerCase() === "j") {
                    console.log(zz);
                  } else {
                    console.log("Nächste Frage");
                  }
                  rl.question("Wollen Sie wissen, wie viel Sie netto monatlich zahlen? : j/n ", (userInput2) => {
                    if (userInput2.toLowerCase() === "j") {
                      console.log(zmoatlich);
                    } else {
                      console.log("Letzte Frage");
                    }
                    rl.question("Wollen Sie wissen, wie viel Ihnen netto monatlich von Ihrem Kredit übrig bleibt? : j/n ", (userInput3) => {
                      if (userInput3.toLowerCase() === "j") {
                        console.log(list);
                      } else {
                        console.log("Danke für Ihre Fragen, viel Spaß mit dem Kredit :)");
                        rl.close();
                      }
                    });
                  });
                });
              }
            } else {
              console.log("Sie müssen mehr monatlich zahlen, es ist nicht gültig (Bitte versuchen Sie es nochmal!)");
              rl.close();
            }
          }
        });
      });
    });
  } catch (error) {
    console.log("Eingabe nicht gültig, bitte geben Sie nur eine Zahl ein!");
    kreditRechner();
  }
}

kreditRechner();
