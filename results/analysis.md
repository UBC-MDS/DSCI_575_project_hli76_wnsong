# Search Comparison Report

Queries compared: BM25, Semantic, Hybrid

## Query: `stainless steel kettle`  
- **Difficulty:** kettle-easy

- BM25 time: 0.111s  •  Semantic time: 0.093s  •  Hybrid time: 0.061s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B01GV52L4U — Danby DKT17C2SSDB 1.7L Kettle Small Appliance, 1.7 L, Stainless Steel (score: 21.983) | B08KGF4Q3H — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.663) | B01GV52L4U — Danby DKT17C2SSDB 1.7L Kettle Small Appliance, 1.7 L, Stainless Steel (score: 0.905) |
| 2 | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 21.000) | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 0.648) | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 0.890) |
| 3 | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 20.253) | B01GV52L4U — Danby DKT17C2SSDB 1.7L Kettle Small Appliance, 1.7 L, Stainless Steel (score: 0.619) | B08KGF4Q3H — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.874) |
| 4 | B08KGF4Q3H — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 20.157) | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.619) | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.865) |
| 5 | B00NN1VC0U — Whirlpool 30" Stainless Steel Gas Cooktop (score: 16.632) | B07G4RQ69X — Stainless Steel 304 Measuring Cup with Scale (16.9oz/500ml, 3 Cups) Large Capacity Kitchen Coffee Cappuccino Latte Art Tea Milk Frothing Jug Pitcher Beaker (score: 0.599) | B077S2TX1T — Portable Tent Wood Burning Stove Military Camping Ice Fishing Cook Heater + Water Kettle - Skroutz (score: 0.668) |

### Observations

- Which method performs better: BM25 and Hybrid perform best. BM25 returns exact matches (e.g., Danby DKT17C2SSDB, SimpleReal pour-over kettle) at the top; Hybrid preserves those top exact matches and gives them the highest combined score.

- Cases where BM25 fails but semantic succeeds: Not in the top results — BM25 already finds exact stainless‑steel items. Semantic returns some related stainless items but also a few non‑kettle stainless items (milk frothing pitchers), so semantic is noisier here.

- Cases where semantic search fails: Semantic surfaced non‑kettle stainless items (milk pitchers, measuring cups) that are conceptually “stainless” but not the user’s intent (a kettle).

- Are top results useful for intent: Yes — BM25 top results are directly relevant. Hybrid keeps the best of both. Semantic alone is less precise for this short, keyword query.

- Strengths / Weaknesses: BM25’s strength is exact keyword matching; semantic can broaden recall but may introduce off‑topic items when the query is short and keyword‑heavy.

---

## Query: `electric kettle with temperature control for tea`  
- **Difficulty:** kettle-medium

- BM25 time: 0.081s  •  Semantic time: 0.024s  •  Hybrid time: 0.092s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 24.937) | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 0.646) | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 0.898) |
| 2 | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 24.275) | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.522) | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.880) |
| 3 | B08VDVTG2B — Electric Cooktop, STULENG 5 Burner Cooktop Stove Top 30 Inch Built In Countertop, Radiant Glass Cooktop Infrared Cooker,Sensor Touch Control 9 Heating Level, Timer, Kid Safety Lock, Wiring Black (score: 22.242) | B08VDVTG2B — Electric Cooktop, STULENG 5 Burner Cooktop Stove Top 30 Inch Built In Countertop, Radiant Glass Cooktop Infrared Cooker,Sensor Touch Control 9 Heating Level, Timer, Kid Safety Lock, Wiring Black (score: 0.515) | B08VDVTG2B — Electric Cooktop, STULENG 5 Burner Cooktop Stove Top 30 Inch Built In Countertop, Radiant Glass Cooktop Infrared Cooker,Sensor Touch Control 9 Heating Level, Timer, Kid Safety Lock, Wiring Black (score: 0.825) |
| 4 | B08KGF4Q3H — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 20.585) | B08KGF4Q3H — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.511) | B08KGF4Q3H — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.791) |
| 5 | B0BTCMQ5DP — Sailnovo 24 Egg Incubator with Automatic Egg Turning and Humidity Control, Incubators for Hatching Eggs with Kettle & Water Can (score: 19.545) | B000RI0HYO — Summit WEL05 30"" Coil Electric Cooktop With 4 Coil Elements Porcelain Enamel Surface Recessed Top Chrome Drip Bowls 230V Electric Cooktop In White (score: 0.497) | B002HMQ1JI — GE JB400SPSS 30" Stainless Steel Electric Smoothtop Range (score: 0.725) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `quiet fast-boiling kettle for small apartment that keeps water warm`  
- **Difficulty:** kettle-complex

- BM25 time: 0.126s  •  Semantic time: 0.025s  •  Hybrid time: 0.141s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B07NL8STS3 — SimpleReal - TAMAGO x ORIGAMI Premium Single Serve Pour Over Coffee Set | Barista Recommended | 12 oz Kettle with Thermometer, Double Wall Glass Cup and Ceramic dripper (score: 22.201) | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 0.586) | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 0.824) |
| 2 | B084C219K2 — ROVSUN 1.6Cu.Ft Beverage Refrigerator Cooler, 60 Can Mini Fridge for Soda Beer Wine Water, Small Drink Dispenser Machine for Office Bar Dorm Apartment with Glass Door, Removable Shelves (score: 20.071) | B08C4TKKR2 — WENKOEBY Portable Instant Cooling Cup, Cooling Cup Electric Quick, Quick Cool Making in 15 Minutes, Home Office Car Cold Drink Machine Small Appliance Kettle(white) (score: 0.527) | B07ZPM3QGT — DADDY COOL Mini Fridge Cooler & Warmer 4 Liter / 6 cans AC/DC. Mini Fridge for Bedroom, Portable Fridge for Home Office, Desk, Desktop, Car SUV or Pickup Truck. Skincare Fridge Makeup Beauty Cosmetic. (score: 0.752) |
| 3 | B07NL7LLBK — SimpleReal - Pour Over Coffee Kettle with Thermometer, Gooseneck Single Serve Mini Kettle for Coffee and Tea, TAMAGO Japanese Style, Stainless Steel body with wooden lid, 12 oz (score: 18.969) | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.498) | B07NL8STS3 — SimpleReal - TAMAGO x ORIGAMI Premium Single Serve Pour Over Coffee Set | Barista Recommended | 12 oz Kettle with Thermometer, Double Wall Glass Cup and Ceramic dripper (score: 0.750) |
| 4 | B0973ZDPQV — COSTWAY Portable Washing Machine, Twin Tub 21Lbs Capacity, Washer(14.4Lbs) and Spinner(6.6Lbs), Laundry Machine with Control Knobs, Built-in Drain Pump, Compact washer for Apartment, RV, Grey (score: 18.719) | B077S2TX1T — Portable Tent Wood Burning Stove Military Camping Ice Fishing Cook Heater + Water Kettle - Skroutz (score: 0.493) | B08KGB9563 — Gevi Milk Frothing Pitcher 12oz/350ml，Stainless Steel Steam Pitchers for Milk Coffee Cappuccino Latte Art,Stainless Steel Powder Shaker with Lid (score: 0.736) |
| 5 | B09C1PZR2C — Full-Automatic Washing Machine 13lbs Portable Compact 2 in 1 Laundry Washer with Drain Pump, 10 Programs 8 Water Level Selections with LED Display, Ideal for Dorm Apartment and Camping (score: 18.297) | B00MNF2FZS — Salton Portable Double Cooktop, 3.45 lb, Black (score: 0.468) | B01GV52L4U — Danby DKT17C2SSDB 1.7L Kettle Small Appliance, 1.7 L, Stainless Steel (score: 0.731) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `personal smoothie blender`  
- **Difficulty:** blender-easy

- BM25 time: 0.048s  •  Semantic time: 0.021s  •  Hybrid time: 0.059s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B094SGZ34H — JOYHANDS Personal Portable Blender for Shakes and Smoothies Mixer USB Rechargeable.Electric Beverage Water Drink Cooler,Smart water bottles for beer cooler 6℃-13℃ Juicer Blender Office and Car 12V (score: 22.909) | B0C6XWV8VG — Xbeauty Nugget Ice Maker-Nugget Ice Maker Countertop Up to 35lbs of Ice a Day with Self-Cleaning,Stainless Steel,Removable Ice Basket&Scoop for Home/Kitchen/Office/Party, Black (score: 0.456) | B094SGZ34H — JOYHANDS Personal Portable Blender for Shakes and Smoothies Mixer USB Rechargeable.Electric Beverage Water Drink Cooler,Smart water bottles for beer cooler 6℃-13℃ Juicer Blender Office and Car 12V (score: 0.855) |
| 2 | B07NQGKTPK — Vita-Mix 015547 Drive Socket Set of 5 (score: 18.561) | B01NAN2AML — Igloo Compact Portable Ice Maker (Stainless Steel) Plus Smoothie Bible Bundle - ICE102ST (score: 0.435) | B01NAN2AML — Igloo Compact Portable Ice Maker (Stainless Steel) Plus Smoothie Bible Bundle - ICE102ST (score: 0.659) |
| 3 | B00KY58ZB2 — Miles Kimball Antique Fruit Appliance Cover Blender (score: 15.164) | B0BG699CZY — SonicPower Bar Ice Maker, Cocktail Quality Clear Ice Cubes, 40lbs Per Day Capacity, Premium Stainless Steel Finishing, Ice Scooper Included (score: 0.427) | B07NQGKTPK — Vita-Mix 015547 Drive Socket Set of 5 (score: 0.655) |
| 4 | B001EY7DI8 — ForeverPRO 9703241 Seal Lid for Whirlpool Blender PS401566 746884 (score: 15.107) | B094SGZ34H — JOYHANDS Personal Portable Blender for Shakes and Smoothies Mixer USB Rechargeable.Electric Beverage Water Drink Cooler,Smart water bottles for beer cooler 6℃-13℃ Juicer Blender Office and Car 12V (score: 0.421) | B000V7309K — WHIRLPOOL 115792 Foot (score: 0.587) |
| 5 | B07F6JQPQX — Igloo Countertop Ice Maker With 26lb Per 24 Hours Capacity (White) Chill Kit With Insulated Cold Cup, Smoothie Bible and 1 YR CPS Enhanced Protection Pack (score: 15.060) | B081ZMYCVM — Frigidaire EFIC229_AMZ Igloo ICE105 Counter Top Compact Ice Maker, Stainless, Silver (score: 0.417) | B00KY58ZB2 — Miles Kimball Antique Fruit Appliance Cover Blender (score: 0.581) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `best blender for smoothies with frozen fruit`  
- **Difficulty:** blender-medium

- BM25 time: 0.079s  •  Semantic time: 0.035s  •  Hybrid time: 0.091s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B00A14MSE6 — Motor Base Replacement for Ninja Kitchen System 1100 WT NJ602 (score: 29.077) | B01FQR5PMY — Hamilton Beach PIM-2-1A Portable Ice Maker, Candy Apple Red (score: 0.561) | B00A14MSE6 — Motor Base Replacement for Ninja Kitchen System 1100 WT NJ602 (score: 0.750) |
| 2 | B094SGZ34H — JOYHANDS Personal Portable Blender for Shakes and Smoothies Mixer USB Rechargeable.Electric Beverage Water Drink Cooler,Smart water bottles for beer cooler 6℃-13℃ Juicer Blender Office and Car 12V (score: 27.884) | B081ZMYCVM — Frigidaire EFIC229_AMZ Igloo ICE105 Counter Top Compact Ice Maker, Stainless, Silver (score: 0.524) | B094SGZ34H — JOYHANDS Personal Portable Blender for Shakes and Smoothies Mixer USB Rechargeable.Electric Beverage Water Drink Cooler,Smart water bottles for beer cooler 6℃-13℃ Juicer Blender Office and Car 12V (score: 0.729) |
| 3 | B00KY58ZB2 — Miles Kimball Antique Fruit Appliance Cover Blender (score: 24.954) | B0BG699CZY — SonicPower Bar Ice Maker, Cocktail Quality Clear Ice Cubes, 40lbs Per Day Capacity, Premium Stainless Steel Finishing, Ice Scooper Included (score: 0.503) | B00KY58ZB2 — Miles Kimball Antique Fruit Appliance Cover Blender (score: 0.679) |
| 4 | B08C73DS42 — (2-Packs) 119411-010-000 Blender Jar Gasket (score: 20.404) | B003EAC9MU — Whirlpool 61002140 Ice Maker Tray (score: 0.490) | B08C73DS42 — (2-Packs) 119411-010-000 Blender Jar Gasket (score: 0.601) |
| 5 | B00GDPSOI6 — RCA 3.2 cu. ft Fridge, Black Erase Board Refrigerator with Neon Markers (score: 16.933) | B07QXHX8NC — KUPPET Ice Maker Machine for Countertop, Portable Automatic Ice Maker with LCD Display, 9 Ice Cubes Ready in 6min, 26 lbs/day - for Parties/Home/Office/Bar, Ice Scoop and Basket (Silver) (score: 0.489) | B00GDPSOI6 — RCA 3.2 cu. ft Fridge, Black Erase Board Refrigerator with Neon Markers (score: 0.541) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `high-power blender for nut butter and ice under $200`  
- **Difficulty:** blender-complex

- BM25 time: 0.092s  •  Semantic time: 0.024s  •  Hybrid time: 0.104s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B07JVDRVDB — DecorRack Stainless Steel Milk Warmer Cup 12 oz Frothing Pitcher for Latte Art Barista Espresso Coffee Maker Milk Pan Foam Blender Decanter, Butter Melting Pot with Handle and Mirror Finish (1 Pack) (score: 19.230) | B0BG699CZY — SonicPower Bar Ice Maker, Cocktail Quality Clear Ice Cubes, 40lbs Per Day Capacity, Premium Stainless Steel Finishing, Ice Scooper Included (score: 0.564) | B07JVDRVDB — DecorRack Stainless Steel Milk Warmer Cup 12 oz Frothing Pitcher for Latte Art Barista Espresso Coffee Maker Milk Pan Foam Blender Decanter, Butter Melting Pot with Handle and Mirror Finish (1 Pack) (score: 0.750) |
| 2 | B09SW59PG1 — Mini Portable Washing Machine, USB High-Power Ultrasonic Turbine Washing Machine, Portable Washing Machine for Travel Business Trip or College Rooms (White) (score: 17.456) | B01H7VHVRO — NutriChef - Countertop Ice Maker Machine - Heavy Duty High-Powered Freezing w/ Built in Freezer Oversized Bucket Includes Ice Shovel Hand Scoop - Easy Touch LED Button Display - PICEM20 (score: 0.560) | B09SW59PG1 — Mini Portable Washing Machine, USB High-Power Ultrasonic Turbine Washing Machine, Portable Washing Machine for Travel Business Trip or College Rooms (White) (score: 0.704) |
| 3 | B08PPBDTK7 — HKKAIS Milk Frothing Pitcher 32Oz Stainless Steel Milk Jug Espresso Steaming Pitcher Barista Cup For Making Coffee Cappuccino Latte Art 32 Oz/900 ML (score: 17.291) | B081ZMYCVM — Frigidaire EFIC229_AMZ Igloo ICE105 Counter Top Compact Ice Maker, Stainless, Silver (score: 0.555) | B08PPBDTK7 — HKKAIS Milk Frothing Pitcher 32Oz Stainless Steel Milk Jug Espresso Steaming Pitcher Barista Cup For Making Coffee Cappuccino Latte Art 32 Oz/900 ML (score: 0.700) |
| 4 | B08JLXDR9Q — 30” Built-in Gas Cook Cooktop Stove LPG/NG Gas Kitchen Burners Multi-Function Cooking High-Power Gas Stove Electronic Ignition with Flameout Protection (score: 17.029) | B005O0D17K — Great Northern Polar Cube Elite White Portable Ice Maker (score: 0.539) | B08JLXDR9Q — 30” Built-in Gas Cook Cooktop Stove LPG/NG Gas Kitchen Burners Multi-Function Cooking High-Power Gas Stove Electronic Ignition with Flameout Protection (score: 0.693) |
| 5 | B09SHQZ2YC — Mini Washing Machine Portable Turbine Washer,USB High-Power in-Line Turbo Washing Machine with Suction Cup,Ultrasonic Waves Speed Control Washer for Travel Business Trip or College Rooms (White) (score: 16.293) | B074B61CGN — NutriChef PICEM15_0 Portable Ice Maker (score: 0.536) | B09SHQZ2YC — Mini Washing Machine Portable Turbine Washer,USB High-Power in-Line Turbo Washing Machine with Suction Cup,Ultrasonic Waves Speed Control Washer for Travel Business Trip or College Rooms (White) (score: 0.674) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `compact toaster oven`  
- **Difficulty:** oven-easy

- BM25 time: 0.053s  •  Semantic time: 0.020s  •  Hybrid time: 0.063s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B00KY5907K — Miles Kimball Antique Fruit Appliance Cover Toaster Oven (score: 18.877) | B00KY5907K — Miles Kimball Antique Fruit Appliance Cover Toaster Oven (score: 0.621) | B00KY5907K — Miles Kimball Antique Fruit Appliance Cover Toaster Oven (score: 0.905) |
| 2 | B08K3SPNL6 — Cooks Innovations NonStick Oven Liner + Toaster Oven Liner & Crisper Sheet Set - Easy to Clean & Heavy Duty Oven Liners for bottom of oven, Oven protector, Reusable Protector Bundle Mats for Kitchen (score: 18.401) | B07MXFXS3H — Smart Oven Cover, ConvectionToaster Oven Cover, Large Size Square Kitchen Appliance Cover, 16.9”Lx16.1”Wx10.6”H, Diamond Collection Kitchen Appliance Case With Two Big Pockets,Provide Yeal Around Protection For Your Appliance (Black) (score: 0.609) | B08K3SPNL6 — Cooks Innovations NonStick Oven Liner + Toaster Oven Liner & Crisper Sheet Set - Easy to Clean & Heavy Duty Oven Liners for bottom of oven, Oven protector, Reusable Protector Bundle Mats for Kitchen (score: 0.867) |
| 3 | B0C6FSYD83 — Premium Liners for Ninja Foodi Air Fryer Bottom of toaster Oven Mat | Compatible with Cuisinart, Ninja Air Fryer SP101 SP102 & Toaster Oven Accessories | Reusable Mat for Flip Up & Non-Stick Tray (score: 17.951) | B0007XLE6O — Warming Rack (score: 0.585) | B01N0D66OL — 3 In 1 Breakfast Station Toaster Oven Griddle Coffee Maker Retro Mini Kitchen (score: 0.854) |
| 4 | B01N0D66OL — 3 In 1 Breakfast Station Toaster Oven Griddle Coffee Maker Retro Mini Kitchen (score: 17.907) | B0011YFQ7Q — GE PB975BMBB ProfileTM 30" Free-Standing Double Oven Rangea (score: 0.552) | B0007XLE6O — Warming Rack (score: 0.846) |
| 5 | B002DI54PI — Delonghi 5318135200 Knob - For Timer & Temperature (score: 17.844) | B003XETOR0 — GE WB44X10016 Stove, Oven, Range Bake Element,BLACK (score: 0.550) | B07MXFXS3H — Smart Oven Cover, ConvectionToaster Oven Cover, Large Size Square Kitchen Appliance Cover, 16.9”Lx16.1”Wx10.6”H, Diamond Collection Kitchen Appliance Case With Two Big Pockets,Provide Yeal Around Protection For Your Appliance (Black) (score: 0.773) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `convection toaster oven for baking small batches`  
- **Difficulty:** oven-medium

- BM25 time: 0.094s  •  Semantic time: 0.013s  •  Hybrid time: 0.106s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B079FRJLHQ — Simple Living Products 3 Piece Air fryer Accessory Set (score: 27.200) | B0007XLE6O — Warming Rack (score: 0.596) | B005JWA9T6 — GE P2B930SETSS Profile 30" Stainless Steel Dual Fuel Sealed Burner Range - Convection (score: 0.836) |
| 2 | B00NN11ZT8 — GE JS750EFES 30" Slate Electric Slide-In Smoothtop Range - Convection (score: 25.017) | B00HFED9NO — Frigidaire FGET3065PBGallery 30" Black Electric Double Wall Oven - Convection (score: 0.588) | B00NN11ZT8 — GE JS750EFES 30" Slate Electric Slide-In Smoothtop Range - Convection (score: 0.827) |
| 3 | B005FNVNDK — GE PGB995SETSS Profile 30" Stainless Steel Gas Sealed Burner Double Oven Range - Convection (score: 23.999) | B005JWA9T6 — GE P2B930SETSS Profile 30" Stainless Steel Dual Fuel Sealed Burner Range - Convection (score: 0.588) | B095YNXNDW — Air Fryer Toaster Oven 13.5 Quart Large Air Fryer Oven 10in1 Convection Oven Airfryer with Rotisserie, Dehydrator & Pizza,Smart Oven-Black (score: 0.807) |
| 4 | B005JWA9T6 — GE P2B930SETSS Profile 30" Stainless Steel Dual Fuel Sealed Burner Range - Convection (score: 23.868) | B00LXTB83K — Verona VEFSGG365NDSS 36" Pro-Style Gas Range with 5 Sealed Burners 2 Turbo-Electric Convection Ovens Manual Clean Infrared Broiler Bell Timer and Storage Drawer in Stainless Steel (score: 0.587) | B08K3SPNL6 — Cooks Innovations NonStick Oven Liner + Toaster Oven Liner & Crisper Sheet Set - Easy to Clean & Heavy Duty Oven Liners for bottom of oven, Oven protector, Reusable Protector Bundle Mats for Kitchen (score: 0.802) |
| 5 | B095YNXNDW — Air Fryer Toaster Oven 13.5 Quart Large Air Fryer Oven 10in1 Convection Oven Airfryer with Rotisserie, Dehydrator & Pizza,Smart Oven-Black (score: 23.286) | B07MXFXS3H — Smart Oven Cover, ConvectionToaster Oven Cover, Large Size Square Kitchen Appliance Cover, 16.9”Lx16.1”Wx10.6”H, Diamond Collection Kitchen Appliance Case With Two Big Pockets,Provide Yeal Around Protection For Your Appliance (Black) (score: 0.568) | B01N4WLTGZ — THOR KITCHEN HRD3606U 36inch Free Standing Stainless Steel Gas Range Electric Oven 6 Burner 5.2 Cu. Ft (score: 0.776) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `countertop oven that fits a 9x13 pan and has air fry mode`  
- **Difficulty:** oven-complex

- BM25 time: 0.123s  •  Semantic time: 0.028s  •  Hybrid time: 0.172s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B09QMBBGNF — 30'' Wall Oven, GASLAND Chef Professional Electric Wall Oven 5.0 Cu.Ft. Convection with Self-cleaning, Sabbath mode, Temperature Probe Included, Hardwire (score: 27.884) | B08TX337VD — Cuisinart AMW-60 3-In-1 Microwave AirFryer Convection Oven with Rubbermaid LunchBlox Lunch Bag, Achim Home Furnishings Buffalo Check Oven Mitt and 5.5-Inch Serr Utility Knife (4 Items) (score: 0.602) | B09QMBBGNF — 30'' Wall Oven, GASLAND Chef Professional Electric Wall Oven 5.0 Cu.Ft. Convection with Self-cleaning, Sabbath mode, Temperature Probe Included, Hardwire (score: 0.883) |
| 2 | B00WH10VQS — Silicone Lid: Large Suction lid 9x13 Baking Lid cmsHome Blue Replacement Lid Premium Food Grade Suction Lid Non-toxic Non-stick (score: 25.673) | B00O5HW10G — GoWISE USA 127.9012 Ming's Mark GW22619 Reusable Oven Mesh Basket (score: 0.588) | B0853F5RVG — Frigidaire Gallery GCRG3060AF 5 Cu.Ft. Stainless Free-Standing Gas Range with Air Fry (score: 0.735) |
| 3 | B08NVBYTZV — Frigidaire GCRI3058AF / GCRI3058AF / GCRI3058AF 30 inch Induction Range with Air Fry (score: 23.195) | B001DK82B0 — Jenn-Air JDR8895AA 30" Double Floating Glass standing Dual-Fuel Ov : Stainless Steel (score: 0.578) | B08PN448L7 — 6.3 cu ft. Smart Wi-Fi Enabled True Convection InstaView® Electric Range with Air Fry (score: 0.724) |
| 4 | B07VCBY8WG — Frigidaire FGEH3047VF Gallery Series 30" Electric Range with 5 Elements, 5.4 Cubic ft. Capacity Convection Oven, in Stainless Steel (score: 23.087) | B07MJHMR6G — Frigidaire FFGW2426UW Frigidaire FFGW2426U 24 Inch Wide 3.3 Cu. Ft. Single Gas Oven with Even Baking Technology (score: 0.576) | B07YZTGYXS — Frigidaire FGGH3047VD 30" Gallery Series Gas Range with 5 Sealed Burners Griddle True Convection Oven Self Cleaning Air Fry Function in Black Stainless Steel (score: 0.723) |
| 5 | B00434YVS6 — Kenyon B41604 6-1/2 and 8-Inch Arctic 2-Burner Cooktop with Analog Control UL, 240-volt, Black (score: 23.073) | B07MXFXS3H — Smart Oven Cover, ConvectionToaster Oven Cover, Large Size Square Kitchen Appliance Cover, 16.9”Lx16.1”Wx10.6”H, Diamond Collection Kitchen Appliance Case With Two Big Pockets,Provide Yeal Around Protection For Your Appliance (Black) (score: 0.561) | B08B3DK2C6 — Frigidaire FGET3069UF 30" Double Electric Wall Oven with Air Fry, 10.2 cu. ft. Capacity, in Stainless Steel. (score: 0.722) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `robot vacuum`  
- **Difficulty:** vacuum-easy

- BM25 time: 0.031s  •  Semantic time: 0.027s  •  Hybrid time: 0.044s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B07RY89Y69 — Robot Vacuum Super Smart (score: 23.671) | B07RY89Y69 — Robot Vacuum Super Smart (score: 0.632) | B07RY89Y69 — Robot Vacuum Super Smart (score: 0.908) |
| 2 | B07XXVJMSR — Hazmemejor Strainer,Perk,HEPA Filter Replacement Fits for LG Smart Robot Vacuum Cleaner (score: 23.490) | B08D115XQ7 — Shark RVBBK700 9ft BotBoundary Strip for Ion Robot Vacuums (score: 0.601) | B09KC8T33Q — Garbage fighter Dust Bin Box for Eufy RoboVac 11S, 30, 30C, 12, 15C, 35C Robot Vacuum Cleaner Part Accessories - High-Capacity Replacement Dustbin for Improved Robot Vacuum Performance (score: 0.880) |
| 3 | B09KC8T33Q — Garbage fighter Dust Bin Box for Eufy RoboVac 11S, 30, 30C, 12, 15C, 35C Robot Vacuum Cleaner Part Accessories - High-Capacity Replacement Dustbin for Improved Robot Vacuum Performance (score: 23.379) | B00O07DS8U — Nispira Vacuum Cleaner Filter Compatible with Neato Robotic Pet & Allergy XV-21 945-0048 Filter, 12 Filters (score: 0.575) | B08D115XQ7 — Shark RVBBK700 9ft BotBoundary Strip for Ion Robot Vacuums (score: 0.855) |
| 4 | B09J4P4SPC — Fayme Roller Brush Side Brush Washable Robot Filter for 360 S5 S7 Robot Vacuum Cleaner Parts Replacement Filter (score: 23.274) | B000EOWA7I — Douglas Quikut ReadiVac 36104 12-Volt Wet/Dry Auto Vacuum (score: 0.571) | B098QXP9HK — Padyrytu Roller Brush Side Brush Washable Robot Filter for 360 S5 S7 Robot Vacuum Cleaner Parts Replacement Filter (score: 0.847) |
| 5 | B098QXP9HK — Padyrytu Roller Brush Side Brush Washable Robot Filter for 360 S5 S7 Robot Vacuum Cleaner Parts Replacement Filter (score: 22.944) | B098XN3JL9 — Ctzrzyt Replacement for Shark IQ Robot R101AE RV1001AE IQ R101 UR1005AE Vacuum,Replaces Parts (score: 0.559) | B091YPHXRF — Bopfimer Side Brush Washable Robot Filter for 360 S6 Robot Vacuum Cleaner Parts Replacement Filter (score: 0.841) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `vacuum for hardwood floors and pet hair`  
- **Difficulty:** vacuum-medium

- BM25 time: 0.073s  •  Semantic time: 0.013s  •  Hybrid time: 0.088s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B009A6OTU2 — acum Cordless Stick Vacuum 23KPa Powerful Suction 6-in-1 Handheld Cleaner, Lightweight & 30min Lasting Runtime, Ideal for Hardwood Floor Carpet Mattress & Pet Hair Cleaning, Black (39) (score: 34.960) | B0895RN5W1 — JoyBros Hard Floor Attachment Brush for Dyson V6 V7 V8 DC58… (score: 0.665) | B0895RN5W1 — JoyBros Hard Floor Attachment Brush for Dyson V6 V7 V8 DC58… (score: 0.905) |
| 2 | B0895RN5W1 — JoyBros Hard Floor Attachment Brush for Dyson V6 V7 V8 DC58… (score: 34.192) | B009A6OTU2 — acum Cordless Stick Vacuum 23KPa Powerful Suction 6-in-1 Handheld Cleaner, Lightweight & 30min Lasting Runtime, Ideal for Hardwood Floor Carpet Mattress & Pet Hair Cleaning, Black (39) (score: 0.591) | B009A6OTU2 — acum Cordless Stick Vacuum 23KPa Powerful Suction 6-in-1 Handheld Cleaner, Lightweight & 30min Lasting Runtime, Ideal for Hardwood Floor Carpet Mattress & Pet Hair Cleaning, Black (39) (score: 0.898) |
| 3 | B07JHKLJFD — Generic Pet Hair Eraser Vacuum Filter Replacement Compatible for Bissell Style 16871 Pet Hair Eraser Upright Vacuum - Fits Vacuum Model 1650 Series (score: 31.249) | B000EOWA7I — Douglas Quikut ReadiVac 36104 12-Volt Wet/Dry Auto Vacuum (score: 0.580) | B07JHKLJFD — Generic Pet Hair Eraser Vacuum Filter Replacement Compatible for Bissell Style 16871 Pet Hair Eraser Upright Vacuum - Fits Vacuum Model 1650 Series (score: 0.816) |
| 4 | B07XMH1ZRB — Wigbow Premium Vacuum Filter Compatible with Bissell Style 16871, 1608861 & 1608860 Pet Hair Eraser Upright Vacuum and Vacuum Model 1650 Series (score: 28.837) | B074Z4X674 — Top Vacuum Parts Replacement For Shop Vac 2 1/2" / 2.5" X 14" Floor Brush 2 PACK (score: 0.549) | B07XMH1ZRB — Wigbow Premium Vacuum Filter Compatible with Bissell Style 16871, 1608861 & 1608860 Pet Hair Eraser Upright Vacuum and Vacuum Model 1650 Series (score: 0.787) |
| 5 | B07FCCYPRT — Aunifun Vacuum Filter Replacement for Bissell 1782 Pet Hair Eraser Handheld Cordless Vacuum Cleaner Replacement Part #1608653, Mesh Frame (score: 27.150) | B071RPBL71 — Bissell Bolt Lithium Pet Lightweight Filter Assembly. Replaces OEM# 1610369 / 161-0369 (score: 0.541) | B07RWV7QJV — 3 Pack Multi Surface Pet Brush Roll 2306A and 3 Pack 1866 Vacuum Filter Compatible with Bissell CrossWave 1785 2306 Wet Dry Vacuum Cleaner (score: 0.756) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Query: `lightweight cordless vacuum for hardwood, pet hair, and stairs under 5 kg`  
- **Difficulty:** vacuum-complex

- BM25 time: 0.132s  •  Semantic time: 0.010s  •  Hybrid time: 0.152s

| Rank | BM25 (ASIN — title) | Semantic (ASIN — title) | Hybrid (ASIN — title) |
|---:|---|---|---|
| 1 | B009A6OTU2 — acum Cordless Stick Vacuum 23KPa Powerful Suction 6-in-1 Handheld Cleaner, Lightweight & 30min Lasting Runtime, Ideal for Hardwood Floor Carpet Mattress & Pet Hair Cleaning, Black (39) (score: 54.159) | B009A6OTU2 — acum Cordless Stick Vacuum 23KPa Powerful Suction 6-in-1 Handheld Cleaner, Lightweight & 30min Lasting Runtime, Ideal for Hardwood Floor Carpet Mattress & Pet Hair Cleaning, Black (39) (score: 0.563) | B009A6OTU2 — acum Cordless Stick Vacuum 23KPa Powerful Suction 6-in-1 Handheld Cleaner, Lightweight & 30min Lasting Runtime, Ideal for Hardwood Floor Carpet Mattress & Pet Hair Cleaning, Black (39) (score: 0.891) |
| 2 | B07FCCYPRT — Aunifun Vacuum Filter Replacement for Bissell 1782 Pet Hair Eraser Handheld Cordless Vacuum Cleaner Replacement Part #1608653, Mesh Frame (score: 39.183) | B000EOWA7I — Douglas Quikut ReadiVac 36104 12-Volt Wet/Dry Auto Vacuum (score: 0.561) | B07FCCYPRT — Aunifun Vacuum Filter Replacement for Bissell 1782 Pet Hair Eraser Handheld Cordless Vacuum Cleaner Replacement Part #1608653, Mesh Frame (score: 0.713) |
| 3 | B07JHKLJFD — Generic Pet Hair Eraser Vacuum Filter Replacement Compatible for Bissell Style 16871 Pet Hair Eraser Upright Vacuum - Fits Vacuum Model 1650 Series (score: 31.249) | B0895RN5W1 — JoyBros Hard Floor Attachment Brush for Dyson V6 V7 V8 DC58… (score: 0.542) | B071RPBL71 — Bissell Bolt Lithium Pet Lightweight Filter Assembly. Replaces OEM# 1610369 / 161-0369 (score: 0.640) |
| 4 | B071RPBL71 — Bissell Bolt Lithium Pet Lightweight Filter Assembly. Replaces OEM# 1610369 / 161-0369 (score: 31.171) | B074Z4X674 — Top Vacuum Parts Replacement For Shop Vac 2 1/2" / 2.5" X 14" Floor Brush 2 PACK (score: 0.521) | B07XMH1ZRB — Wigbow Premium Vacuum Filter Compatible with Bissell Style 16871, 1608861 & 1608860 Pet Hair Eraser Upright Vacuum and Vacuum Model 1650 Series (score: 0.617) |
| 5 | B07XMH1ZRB — Wigbow Premium Vacuum Filter Compatible with Bissell Style 16871, 1608861 & 1608860 Pet Hair Eraser Upright Vacuum and Vacuum Model 1650 Series (score: 28.837) | B07KVZGP1H — Vacuum Pump, DC12V 12W Mini Vacuum Pump Water Air Gas Vacuum Pump 81KPa Flow 10L/min Oilless Vacuum Pump, Mini Air Pump Motor (score: 0.514) | B0895RN5W1 — JoyBros Hard Floor Attachment Brush for Dyson V6 V7 V8 DC58… (score: 0.611) |

### Observations

- Overlap: 
- Relevance notes: 
- Strengths / Weaknesses: 

---

## Overall Evaluation

- Summary and recommendations.
