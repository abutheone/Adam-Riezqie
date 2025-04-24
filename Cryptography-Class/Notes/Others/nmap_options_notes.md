
# Nmap Options Notes

## Basic Syntax
```sh
nmap [options] <target>
```

## Common Nmap Options

### `-sV`
- **Description:** Attempts to determine the version of services running on open ports.
- **Example Usage:**
```sh
nmap -sV <target>
```

### `-p <port-range>`
- **Description:** Specify ports to scan. The default scan checks the most common ports.
- **Example Usage:**
```sh
nmap -p 22,80,443 <target>
nmap -p 1-1024 <target>
```

### `-sS` (TCP SYN Scan)
- **Description:** A stealth scan method that sends SYN packets and waits for responses. This is faster than a full TCP connect scan.
- **Example Usage:**
```sh
nmap -sS <target>
```

### `-O` (Operating System Detection)
- **Description:** Attempts to determine the operating system of the target.
- **Example Usage:**
```sh
nmap -O <target>
```

### `-A` (Aggressive Scan)
- **Description:** Performs OS detection, version detection, script scanning, and traceroute.
- **Example Usage:**
```sh
nmap -A <target>
```

### `-T<0-5>` (Timing Options)
- **Description:** Set the scan timing. Ranges from 0 (slowest) to 5 (fastest). Increasing speed might result in more detectable scans.
- **Example Usage:**
```sh
nmap -T4 <target>
```

### `-v` (Verbose Output)
- **Description:** Provides more detailed information about the scan.
- **Example Usage:**
```sh
nmap -v <target>
```

### `-oN <file>` (Output to Normal File)
- **Description:** Save the scan results to a normal text file.
- **Example Usage:**
```sh
nmap -oN scan_results.txt <target>
```

### `-oX <file>` (Output to XML File)
- **Description:** Save the scan results to an XML file.
- **Example Usage:**
```sh
nmap -oX scan_results.xml <target>
```

### `--script <script>` (Use Nmap Scripts)
- **Description:** Runs Nmap's script engine to perform additional tasks like vulnerability scanning.
- **Example Usage:**
```sh
nmap --script http-vuln-cve2014-3704 <target>
```

### `--top-ports <num>`
- **Description:** Scan the most common ports. Useful for quickly identifying open services.
- **Example Usage:**
```sh
nmap --top-ports 10 <target>
```

### `-Pn` (No Ping Scan)
- **Description:** Treats the target as up and doesn't perform a host discovery ping. Useful for scanning hosts behind firewalls.
- **Example Usage:**
```sh
nmap -Pn <target>
```

### `-f` (Fragmentation)
- **Description:** Send fragmented packets to evade detection.
- **Example Usage:**
```sh
nmap -f <target>
```

### `--source-port <port>`
- **Description:** Specify a source port for the scan.
- **Example Usage:**
```sh
nmap --source-port 53 <target>
```

### `--reason`
- **Description:** Displays the reason why Nmap considers a port open or closed.
- **Example Usage:**
```sh
nmap --reason <target>
```

## References
1. [Nmap Documentation](https://nmap.org/book/man.html)
2. [Nmap Cheatsheet](https://github.com/enaqx/awesome-pentest#nmap)
