<h1 align="center">
  <br>
  <a href="https://github.com/MrRenoX/Reno_Bomber"><a href="https://imgbb.com/"><img src="https://i.ibb.co/mVGFCN8W/reno-bomber.png" alt="reno-bomber"  width="220"/></a>
  <br>
  Reno_Bomber 
  <br>
</h1>

<p align="center">Reno_Bomber — A lightweight SMS/Call <strong>testing & research</strong> utility (educational & authorized testing only).</p>

---

## ⚠️ Important — Read Before Using

**Reno_Bomber is intended strictly for learning, API testing, and research.**  
Any misuse of this tool (harassment, spamming, illegal activity) is strictly prohibited.  
By using this repository, you agree to follow local laws, API Terms of Service, and obtain explicit consent before testing on any phone number or service.This Repo is created for Fun TOOL. 
The author and contributors are **not responsible** for any misuse.

---

## Project Overview

Reno_Bomber is a small Python-based toolkit For call and SMS Bombing. 
This is Created for Research Perpose only.
This tool is Work only on Indian Number.
fast and secure SMS and call Bombing on Indian Number.

---

## Features

- Termux Based TOOL. Run Only on Termux
- Maximum  integrated messaging and calling APIs included with JSON
- Super-fast bombing with multithreading, fast(Abuse Protection)
- Only Work on the Indian Numbers,API Support on the Indian Number.
- Flexible with addition of newer APIs with the help of JSON documents
- Actively supported by the developers with frequent updates and bug-fixes
- Intuitive auto-update feature and notification fetch feature included
- Modular codebase and snippets can be easily embedded in other program

---

## Compatibility

- Python 3.8+ recommended  
Check version:
```bash
python3 --version
```
- If Version 3.8+ (recommended) then Reno Bomber working well On Indian Number.

## Usage:

#### Currently Avilable only on Termux


#### For Termux

To use the Reno Bomber type the following commands in Termux:
```shell script
pkg install git -y

pkg install python -y
 
git clone https://github.com/MrRenoX/Reno_Bomber.git

cd Reno_Bomber

pip install -r requirements.txt

python Reno_bomber.py
```



## Processes of Reno Bomber – Visual Overview

<p align="center">
  <a href="https://ibb.co/1GT6mJDz" target="_blank">
    <img src="https://i.ibb.co/yFqSQBw4/IMG-20251001-110753.jpg" alt="Image 1" width="220" style="margin:10px; border-radius:10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
  </a>
  <a href="https://ibb.co/hSJH2s7" target="_blank">
    <img src="https://i.ibb.co/6k7bDYn/IMG-20251001-110740.jpg" alt="Image 2" width="220" style="margin:10px; border-radius:10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
  </a>
  <a href="https://ibb.co/nMbKK6F6" target="_blank">
    <img src="https://i.ibb.co/1GL447k7/IMG-20251001-110716.jpg" alt="Image 3" width="220" style="margin:10px; border-radius:10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
  </a>
  <a href="https://ibb.co/pr5t9NhL" target="_blank">
    <img src="https://i.ibb.co/WpjbY7V2/IMG-20251001-110700.jpg" alt="Image 4" width="220" style="margin:10px; border-radius:10px; box-shadow: 0px 4px 12px rgba(0,0,0,0.3); transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.1)'" onmouseout="this.style.transform='scale(1)'" />
  </a>
</p>

<p align="center">
  <em>Click on any image to view in full size</em>
</p>

---

### Image Descriptions & Short Tutorials

#### 1️⃣ Input Collection
![Image 1](https://i.ibb.co/yFqSQBw4/IMG-20251001-110753.jpg)  
**Description:** Collects all required inputs like Whats user want to Choose like(SMS/CALL/MAIL).

**Tutorial:** Data is gathered from input files or user interface, Select the Correct Input Like(SMS/CALL/MAIL).  

#### 2️⃣ Data Preparation
![Image 2](https://i.ibb.co/6k7bDYn/IMG-20251001-110740.jpg)  
**Description:** Collects all required inputs like Phone Number, Number of Time , Time of delay . 

**Tutorial:** Python scripts ensure all templates are structured correctly, placeholders are replaced, and everything is queued systematically.  

#### 3️⃣ Dispatch Engine
![Image 3](https://i.ibb.co/1GL447k7/IMG-20251001-110716.jpg)  
**Description:** Handles sending messages or making calls based on configured channels.  

**Tutorial:** The engine iterates through input data, dispatches messages using APIs/SDKs, and records the status of each action.  

#### 4️⃣ Monitoring & Logging
![Image 4](https://i.ibb.co/WpjbY7V2/IMG-20251001-110700.jpg)  
**Description:** Tracks activities in real-time and generates logs for performance review and debugging.  

**Tutorial:** Logs include timestamps, success/failure stats, and optional feedback reports for evaluation.


## Contributing to Reno Bomber

We welcome contributions from developers and researchers to improve Reno Bomber. If you want to add new features, APIs, or improve existing functionality, follow the guidelines below:

---

### How You Can Contribute

1. **Add New APIs**  
   - You can integrate new **SMS API, call API, or MAIL API**.  
   - Make sure to follow the same modular structure (`apidata.json).
   - When integrate new api Please make moduler like sno,Type api like(sms|call|mail).
   - Provide proper **documentation** for any new API integration.

2. **Extend Functionality**  
   - Add new **APIS , and add in the (apidata.json) and fixed in python file**.
   - Fixed and improve the Python file.
   - If Comfertable in BASH Scripting Please Add Bash MENU.  
   - Improve the monitoring, reporting, or error handling mechanisms.  

3. **Improve Existing Modules**  
   - Refactor code for better performance, reliability, and readability.  
   - Add unit tests for new or existing functions.  
   - Optimize data validation and input handling.

4. **Submit Your Contributions**  
   - Fork the repository.  
   - Create a new branch:  
     ```bash
     git checkout -b feature/your-feature-name
     ```  
   - Make your changes and test thoroughly.  
   - Commit your changes with clear messages:  
     ```bash
     git commit -m "Add [feature/API name] for SMS/Call/Email"
     ```  
   - Push your branch and open a Pull Request (PR).  

5. **Guidelines for Code Quality**  
   - Follow **PEP8 / Python style guide**.  
   - Include **docstrings** and comments for clarity.  
   - Ensure new modules or APIs do **not break existing functionality**.  

---

### Examples of Contributions

- Adding a **new SMS API** module with retry logic.  
- Integrating **MAIL API** for mail bombing.  
- Implementing **call API** for call bombing.  
- Enhancing **logging and monitoring** with json file.
- Add BASH Scripting for Professional Menu and Automation.

---

> **Note:** All contributions must comply with responsible use policies. Avoid adding features that enable spam, harassment, or illegal activity. Reno Bomber is intended strictly for **educational and research purposes**.




## Support

Please Support our Tool  
Contributions, issues, and feature requests are welcome!  
Give a ★ if you like this project!

<p align="right"> Last Tool Update: 10/01/2025 </p>




