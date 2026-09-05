#!/data/data/com.termux/files/usr/bin/bash
set -e

export DISPLAY=:1
export PULSE_SERVER=127.0.0.1

echo "======================================"
echo "        TERMUX X11 STARTUP"
echo "======================================"

# Start Termux:X11 server
termux-x11 :1 >/tmp/termux-x11.log 2>&1 &
X11_PID=$!

sleep 3

# Start Debian if installed
if proot-distro list 2>/dev/null | grep -q "debian"; then
    echo "[+] Starting Debian..."
    proot-distro login debian --shared-tmp -- bash -lc '
        export DISPLAY=:1
        export PULSE_SERVER=127.0.0.1
        export XDG_RUNTIME_DIR=/tmp/runtime-$USER
        mkdir -p "$XDG_RUNTIME_DIR"
        chmod 700 "$XDG_RUNTIME_DIR"

        if command -v dbus-launch >/dev/null 2>&1; then
            dbus-launch --exit-with-session xfce4-session
        else
            xfce4-session
        fi
    '
else
    echo "[!] Debian is not installed."
    echo "Install it with:"
    echo "    proot-distro install debian"
fi

wait "$X11_PID"
