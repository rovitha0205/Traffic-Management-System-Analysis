# Chennai Traffic Dataset – Data Preprocessing Project

This repository demonstrates a **complete data preprocessing workflow**
using a regional traffic dataset from the **Chennai Metropolitan Area, Tamil Nadu**.

The focus of this project is **data cleaning and preparation**, not visualization or modeling.

---

##  Datasets Included

### 1. Raw Dataset (Uncleaned)
**File:** `chennai_raw_uncleaned_dataset.xlsx`

This dataset intentionally contains real-world data issues such as:
- Missing values
- Inconsistent categorical labels
- Extra whitespaces in text fields
- Mixed casing (yes / Yes / NO)
- Incomplete IDs

This simulates how raw data is typically received in real projects.

---

### 2. Cleaned Dataset
**File:** `chennai_traffic_cleaned.xlsx`

This dataset is the processed version of the raw data and is:
- Structured
- Consistent
- Ready for analysis or visualization

---

##  Data Preprocessing Steps

The following preprocessing steps were applied using Python and Pandas:

### Step 1: Standardize State Names
- Converted inconsistent values like `TN` and `TamilNadu`
- Standardized to `Tamil Nadu`

### Step 2: Clean Zone / District Names
- Removed trailing and leading whitespaces
- Ensured uniform text formatting

### Step 3: Handle Missing IDs
- Filled missing IDs using forward-fill method
- Ensures each record has a valid identifier

### Step 4: Normalize ITS Deployment Values
- Converted values such as `yes`, `Yes`, `NO` into standard categories:
  - `Yes`
  - `Partial`
  - `No`
- Missing values replaced with `No`

### Step 5: Handle Missing Numerical Values
- Columns affected:
  - Population
  - Traffic Signal Coverage
  - Number of Cameras
  - Commute Time
- Missing values filled using **median imputation**
- Median chosen to reduce impact of outliers

### Step 6: Rename Columns
- Converted column names into a consistent, readable schema
- Improves clarity and usability for downstream tasks

### Step 7: Save Cleaned Dataset
- Final cleaned dataset saved as:
  `chennai_traffic_cleaned.xlsx`

---

## ⚙️ How to Run Preprocessing

```bash
python preprocessing.py
