# Ecoline — Шымкент бояу зауыты

## 📁 Файл структурасы

```
ecoline/
├── index.html          ← Негізгі HTML
├── css/
│   └── style.css       ← Барлық стильдер
├── js/
│   ├── main.js         ← Негізгі логика
│   └── analytics.js    ← Google Analytics
└── images/
    ├── fasad.jpg        ← Өнім фотолары
    ├── gidro.jpg
    └── ...
```

## 🚀 Іске қосу

1. VS Code-та папканы ашыңыз
2. Live Server плагинін орнатыңыз
3. index.html → оң батырма → "Open with Live Server"

## 📝 Өзгертулер

### Баға өзгерту
`js/main.js` файлында `PRODUCTS` массивін тауып:
```js
{n:'Фасадтық бояу Ecoline', price: 11000, ...}
```

### Фото қосу
`images/` папкасына фото салып, `main.js`-те:
```js
const PH = {
  'Фасадтық бояу Ecoline': 'images/fasad.jpg',
  ...
}
```

### Google Analytics
`js/analytics.js` файлында `G-XXXXXXXXXX` орнына ID қойыңыз.

## 📞 Байланыс
- WhatsApp: +7 777 005 07 57
- Instagram: @ecoline_kz
