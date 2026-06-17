# Terminal Cheat Sheet — Day 1

## Open the terminal

| OS | How to open |
|---|---|
| macOS | Press `⌘ + Space`, type **Terminal**, press Enter |
| Linux | Press `Ctrl + Alt + T` |
| Windows (WSL) | Press `Win + X`, choose **Windows Terminal** or **Ubuntu** |

---

## First commands

```bash
pwd
ls
mkdir ife-day1
cd ife-day1
```

---

## Hello, World

```bash
echo "Hello, world!"
```

## Personalized greeting

```bash
echo "Hello, world! My name is [YOUR NAME]."
```

Example:

```bash
echo "Hello, world! My name is Maya."
```

---

## Fun commands

```bash
figlet -f slant "Hello"
cowsay "Hello, world!"
toilet --gay "Hello"
echo "Hello" | lolcat
```

---

## Optional script version

Create a script:

```bash
cat > hello.sh <<'EOF'
echo "Hello, world! My name is [YOUR NAME]."
EOF
```

Make it executable:

```bash
chmod +x hello.sh
```

Run it:

```bash
./hello.sh
```

---

## If you are on Windows and WSL is slow

Use the cloud-terminal fallback:

- GitHub Codespace, or
- Replit workspace

Ask a TA if you need help switching.
