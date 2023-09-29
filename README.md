# port-killer
**Port-Killer is a cross-platform python programme which can be used to disable USB ports of Linux and Windows. With growing concerns about data security and the need to safeguard sensitive information, this programme offers an essential tool to prevent unauthorized USB device connections and protect your system's integrity.**<br><br>
![version](https://img.shields.io/badge/version-1.0-blue)
![python-version](https://img.shields.io/badge/python-3.0+-blue)<br>
![os-support](https://img.shields.io/badge/Linux-Supported-green)
![os-support](https://img.shields.io/badge/Windows-Supported-green)
### Download
```
git clone https://github.com/l3urk/port-killer.git
```
**OR**
```
wget https://github.com/l3urk/port-killer/archive/main.zip
```
### Usage
#### Installing requirements
```
cd port-killer
pip install -r requirements.txt
```
#### Running the program
> [!NOTE]
> For running this programme you will need `sudo` (in linux) or `Administrator` (in windows) privileges.
##### Linux :-
```
sudo python port-killer.py
```
##### Windows :-
If your terminal has `admin` privileges
```
python port-killer.py
```
If your command prompt is not running as `admin`
```
Start-Process -FilePath "python.exe" -ArgumentList ".\port-killer.py" -Verb RunAs
```
