import TheBOT from './TheBOT.js';

(function () {

    "use strict";

    // Verry safe crash handling ;)
    // process.on('uncaughtException', function (err) {
    //     Log.log("[!Pokedex!] Error: ");
    //     Log.log(err);
    // });

    // Start the pokedex bot!
    let thebot = new TheBOT();
    thebot.init();

}());
