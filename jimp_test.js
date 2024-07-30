// const Jimp = require('jimp');
// const dataset = require("./dataset.json");

// const symbols =
//   " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
//     .split("")
//     .concat(["margin"]);


// const resolvedPromises = [];

// async function processImages() {
//     for (let i = 0; i < symbols.length; i += 1) {
//         for (let j = 0; j < 6; j += 1) {
//             const jimpObject = await Jimp.read(Buffer.from(dataset[i][j]));
//             resolvedPromises.push(jimpObject);
//             dataset[i][j] = await jimpObject.getBufferAsync(Jimp.MIME_PNG);
//             //save the image to the filesystem 
//             jimpObject.write(`./output/${symbols[i]}_${j}.png`);
//         }
//     }
// }

// processImages();

// baseado no seguinte texto, gere um pdf com as imagens geradas
// "The quick brown fox jumps over the lazy dog"
// cada letra deve ser uma imagem diferente
// cada palavra deve ser separada por um espaço
// cada espaço deve ser uma imagem diferente
// o texto deve ser centralizado na página
// a fonte deve ser a mesma usada no dataset
// a cor do texto deve ser preta
// o tamanho da fonte deve ser 24
// o pdf deve ser salvo no diretório output com o nome "output_hahaha.pdf"
// o pdf deve ter 1 cm de margem em todas as bordas

// Path: jimp_test.js
const Jimp = require('jimp');
const dataset = require("./dataset.json");
const fs = require('fs');
const PDFDocument = require('pdfkit');

const symbols = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        .split("")
        .concat(["margin"]);

const resolvedPromises = [];

async function processImages() {
    for (let i = 0; i < symbols.length; i += 1) {
        for (let j = 0; j < 6; j += 1) {
            const jimpObject = await Jimp.read(Buffer.from(dataset[i][j]));
            resolvedPromises.push(jimpObject);
            dataset[i][j] = await jimpObject.getBufferAsync(Jimp.MIME_PNG);
            //save the image to the filesystem 
            jimpObject.write(`./output/${symbols[i]}_${j}.png`);
        }
    }
}

async function generatePDF() {
    const doc = new PDFDocument({
        size: 'A4',
        margin: 28
    });
    doc.pipe(fs.createWriteStream('./output/output_hahaha.pdf'));

    const text = "The quick brown fox jumps over the lazy dog";
    const words = text.split(" ");
    const font = await Jimp.loadFont(Jimp.FONT_SANS_32_BLACK);
    doc.font(font);
    doc.fontSize(24);
    doc.text(text, {
        align: 'center'
    });

    doc.end();
}

processImages().then(() => generatePDF());





