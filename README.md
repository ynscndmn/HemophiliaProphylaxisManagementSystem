

# 🩸 Hemophilia Prophylaxis Management System (🇺🇸 ENGLISH VERSION)

A comprehensive clinical decision-support and cost analysis system implemented in Python.

This project was developed to simulate how the Social Security Institution (SSI) evaluates hemophilia patients for prophylaxis eligibility, calculates medication requirements, optimizes vial distribution, and performs large-scale statistical analysis. The system integrates medical rules, algorithmic optimization, cost modeling, and structured data aggregation.

---

## General Medical Background

### Hemophilia Disease
Clotting factors are proteins that play a critical role in blood coagulation. Deficiency of these factors results in bleeding disorders known as hemophilia.

The most common types:
* **Hemophilia A** → Factor VIII deficiency
* **Hemophilia B** → Factor IX deficiency

### Severity Classification
In healthy individuals, clotting factor levels range between 50% and 150%. Hemophilia severity is determined based on the factor level in the blood:

| Factor Level (%) | Severity |
| :--- | :--- |
| < 1 | Severe |
| ≥ 1 and ≤ 5 | Moderate |
| > 5 and < 50 | Mild |



### Treatment Principles
Patients receive medications either during bleeding episodes or as a preventive treatment (prophylaxis).

### Factor Effectiveness
* **1 IU/kg of Factor VIII** → Increases blood level by approximately **2%**.
* **1 IU/kg of Factor IX** → Increases blood level by approximately **1%**.

### Production Types & Pricing
* **Plasma-derived factor (P):** $0.30 per IU
* **Recombinant factor (R):** $0.40 per IU

### Inhibitor Presence
If the antibody level is **5 BU or higher**, the patient is considered inhibitor-positive. Inhibitor varlığı ilacın etkinliğini azaltır veya tamamen ortadan kaldırır.

---

##  Prophylaxis Rules

A patient is eligible for prophylaxis if they meet the following criteria:
1. **Severe** hemophilia **AND** inhibitor-negative.
2. **Moderate** hemophilia **AND** experienced an average of three or more bleeding episodes per month in the past year (**≥ 36 total**) **AND** inhibitor-negative.

### Administration
* **Hemophilia A:** 3 times per week.
* **Hemophilia B:** 2 times per week.
* **Target Factor Level:** Each dose must raise the factor level to **40%**.

---

##  Dose Calculation Model

The minimum required dose per injection is calculated as follows:

`Minimum Dose (IU) = (Weight * (40 - Current Factor Level)) / Increase Factor`

**Increase Factor:**
* **2** for Factor VIII (Hemophilia A)
* **1** for Factor IX (Hemophilia B)

---

##  Vial Optimization Strategy

Available vial sizes: **2000, 1500, 1000, 500, 250 IU**.

The program applies a **greedy algorithm** (largest to smallest) to:
* Minimize vial count.
* Fully satisfy the dose requirement by rounding up to the nearest vial size.
* Avoid under-dosing.

The system calculates single-dose distribution, 4-week totals per patient, and global 4-week totals for all patients.

---

##  Cost Modeling

The system performs the following financial calculations:
* 4-week total medication cost.
* Annual cost (13 × 4-week periods).
* Total SSI reimbursement amounts.
* Average annual medication amount per patient (IU).
* Average annual cost per patient ($).

---

##  Program Output

### For Each Patient
After data entry, the program provides a detailed summary:
* TR identification number and Name/Surname.
* Disease type (A/B) and Severity level.
* Prophylaxis eligibility status.
* **If eligible:** Factor type, weekly frequency, minimum required dose vs. actual dose, vial distribution (both single & 4-week), and total 4-week cost.

### Final Statistical Report
Once all data entry is complete, the system generates a global report:
* **Patient Distribution:** Total counts and percentages for A/B types and all severity levels.
* **Inhibitor Analysis:** Percentage of inhibitor presence (calculated separately for A and B).
* **Prophylaxis Analysis:** Percentage of patients on prophylaxis and targeted analysis for moderate cases.
* **Medication Usage:** Total IU for Factor VIII/IX (Plasma vs. Recombinant) and global 4-week/1-year costs.
* **Averages:** Global annual IU and cost averages per patient.
* **Maximum Value Tracking:** Identification of patients with the highest usage (IU) and highest cost ($).

---

##  Technical Design

The project demonstrates key software engineering and programming concepts:
* **Structured programming principles** and meaningful variable naming.
* **Mathematical dose computation** and greedy optimization logic.
* **Input validation** with strict constraints (e.g., weight, factor levels, data types).
* **Pure Python 3 implementation** using nested loops without relying on external libraries.

---



##  Academic Context
Course: Algorithms and Programming

Project Title: Hemophilia Prophylaxis Management System

Author: Yunus Can Duman

Institution: Ege University - Computer Engineering










# 🩸 Hemofili Profilaksi Yönetim Sistemi (🇹🇷 TÜRKÇE VERSİYON)

Bu proje, Sosyal Güvenlik Kurumu'nun (SGK) hemofili hastalarını profilaksi (önleyici tedavi) uygunluğu açısından nasıl değerlendirdiğini simüle etmek, ilaç gereksinimlerini hesaplamak, flakon dağıtımını optimize etmek ve büyük ölçekli istatistiksel analizler yapmak amacıyla Python dilinde geliştirilmiş bir klinik karar destek ve maliyet analiz sistemidir.

---

##  Genel Tıbbi Arka Plan

### Hemofili Hastalığı
Pıhtılaşma faktörleri, kanın pıhtılaşmasında kritik rol oynayan proteinlerdir. Bu faktörlerin eksikliği, hemofili olarak bilinen kanama bozukluklarına yol açar.

**En yaygın türler:**
* **Hemofili A** → Faktör VIII eksikliği
* **Hemofili B** → Faktör IX eksikliği

### Şiddet Sınıflandırması
Sağlıklı bireylerde pıhtılaşma faktör seviyeleri %50 ile %150 arasındadır. Hemofili şiddeti, kandaki faktör düzeyine göre belirlenir:

| Faktör Seviyesi (%) | Şiddet |
| :--- | :--- |
| < 1 | Ağır (Severe) |
| ≥ 1 ve ≤ 5 | Orta (Moderate) |
| > 5 ve < 50 | Hafif (Mild) |



### Faktör Etkinliği ve Fiyatlandırma
* **Faktör VIII (A):** 1 IU/kg doz, kan seviyesini **%2** artırır.
* **Faktör IX (B):** 1 IU/kg doz, kan seviyesini **%1** artırır.
* **Plazma kaynaklı faktör (P):** 0.30 $ / IU
* **Rekombinant faktör (R):** 0.40 $ / IU

---

##  Profilaksi Kuralları

Bir hastanın profilaksiye (koruyucu tedavi) uygun sayılması için aşağıdaki kriterleri karşılaması gerekir:
1. **Ağır** hemofili **VE** inhibitör negatif olması.
2. **Orta** hemofili **VE** son bir yılda ayda ortalama en az 3 kanama atağı (**toplam ≥ 36**) **VE** inhibitör negatif olması.

### Uygulama Şeması
* **Hemofili A:** Haftada 3 kez uygulama.
* **Hemofili B:** Haftada 2 kez uygulama.
* **Hedef:** Her doz, faktör seviyesini **%40**'a yükseltmelidir.

---

##  Doz ve Flakon Hesaplama

### Doz Formülü
Enjeksiyon başına gereken minimum doz şu formülle hesaplanır:

$$\text{Minimum Doz (IU)} = \frac{\text{Ağırlık} \times (40 - \text{Mevcut Faktör Seviyesi})}{\text{Artış Faktörü}}$$

### Flakon Optimizasyonu
Sistemde **2000, 1500, 1000, 500, 250 IU** boyutlarında flakonlar tanımlıdır. Program, **Greedy Algorithm** kullanarak:
* Toplam flakon sayısını minimize eder.
* Doz ihtiyacını tam karşılamak için her zaman bir üst flakon kombinasyonuna yuvarlar.
* Eksik doz riskini ortadan kaldırır.

---

##  Program Özellikleri ve Çıktılar

Program çalıştırıldığında iki aşamalı bir rapor sunar:

1.  **Bireysel Analiz:** Her hasta girişi sonrası TC No, hastalık tipi, şiddet seviyesi, profilaksi uygunluğu ve uygunsa detaylı ilaç/maliyet dökümü.
2.  **Genel İstatistik Raporu:** Veri girişi bittiğinde;
    * Hastalık tipi ve şiddet dağılımları (yüzdesel).
    * İnhibitör prevalansı.
    * Toplam ilaç tüketimi (IU) ve maliyet analizi ($).
    * Yıllık SGK geri ödeme projeksiyonları.
    * En yüksek maliyetli ve en yüksek doz kullanan hasta takibi.

---

##  Teknik Tasarım

* **Dil:** Pure Python 3
* **Algoritma:** Greedy Search (Flakon Dağıtımı için)
* **Veri Yapıları:** Dinamik listeler ve iç içe döngüler.
* **Giriş Kontrolü:** Hatalı veri girişini engelleyen validasyon mekanizması.

---
##  Akademik Bağlam

Ders: Algoritmalar ve Programlama

Proje Başlığı: Hemofili Profilaksi Yönetim Sistemi

Yazar: Yunus Can Duman

Kurum: Ege Üniversitesi - Bilgisayar Mühendisliği
