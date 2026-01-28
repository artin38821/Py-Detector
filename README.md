🛡️ PySentinel: Static File Analyzer
This project is a simple yet elusive way to grab a file and read off its information. It allows us Junior Analysts to automate tens upon thousands of work with just one search in the system without executing the file, risking our safety and protection as agents.

🔍 How it Works:
Safety First: The script opens the target file in "Read-Binary" mode. This allows it to maintain security, as the file can't actually do anything. It ultimately determines whether it's harmful or not.

SHA 256: Every file has a SHA-256 hash that is basically the footprint of the file. The tool looks over databases and looks at known malware that can be festering around.

Hidden Text: The tool looks over hidden text in the file and flags certain words such as powershell, ncat, and .exe. A lot of files today are labelled as safe, but unexpectedly have malicious exe files that can inflict viruses and other types of malware on your computer. My tool disallows that to ever happen.

Conclusive: When it finishes reading off the code in a text file, it gives you a verdict whether or not the file is a true positive or a false positive.

🚀 HOW TO RUN (IMPORTANT)
Open the file in PowerShell (or any coding platform).

RUN: python c:\Users\User\Downloads\file_checker.py.

Prompt: Then it will say "Enter path to file to scan".

Input: Copy the file path and paste it into the code.

Alert: It should alert you based on certain keywords it finds, if it's a true positive or negative.

(Comments included in code, soon :) )



