#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "=============================================="
echo "       PERFECT-OS & AI — X11 INSTALL"
echo "=============================================="

pkg update -y
pkg upgrade -y
pkg install -y x11-repo termux-x11-nightly proot-distro dbus git rsync python

termux-setup-storage || true

# Install Debian if necessary
if ! proot-distro list 2>/dev/null | grep -q "debian"; then
    proot-distro install debian
fi

# Install graphical environment inside Debian
proot-distro login debian --shared-tmp -- bash -lc '
    apt update
    DEBIAN_FRONTEND=noninteractive apt upgrade -y
    DEBIAN_FRONTEND=noninteractive apt install -y \
        xfce4 \
        xfce4-goodies \
        dbus-x11 \
        thunar \
        mousepad \
        xterm \
        git \
        rsync \
        curl \
        wget \
        python3 \
        python3-pip \
        python3-venv \
        build-essential

    mkdir -p /root/Perfect-OS-AI/{projects,apps,ai,scripts,data,termux}
'

# Copy Termux projects into the Debian workspace
if [ -d "$HOME/projects" ]; then
    cp -a "$HOME/projects/." \
    "$PREFIX/var/lib/proot-distro/installed-rootfs/debian/root/Perfect-OS-AI/termux/" \
    2>/dev/null || true
fi

# Copy common projects if they exist
for DIR in banker-ai Tower Perfect-OS-AI scripts github; do
    if [ -d "$HOME/$DIR" ]; then
        mkdir -p \
        "$PREFIX/var/lib/proot-distro/installed-rootfs/debian/root/Perfect-OS-AI/termux/$DIR"
        cp -a "$HOME/$DIR/." \
        "$PREFIX/var/lib/proot-distro/installed-rootfs/debian/root/Perfect-OS-AI/termux/$DIR/" \
        2>/dev/null || true
    fi
done

# Start X11
pkill -f 'termux-x11 :1' 2>/dev/null || true
sleep 2

termux-x11 :1 >/tmp/perfect-x11.log 2>&1 &
sleep 4

# Open Android Termux:X11 app
am start -n com.termux.x11/.MainActivity >/dev/null 2>&1 || true
sleep 2

# Start XFCE
proot-distro login debian --shared-tmp -- bash -lc '
    export DISPLAY=:1
    export XDG_CURRENT_DESKTOP=XFCE
    export XDG_SESSION_DESKTOP=xfce
    export XDG_RUNTIME_DIR=/tmp/perfect-runtime

    mkdir -p "$XDG_RUNTIME_DIR"
    chmod 700 "$XDG_RUNTIME_DIR"

    dbus-launch --exit-with-session startxfce4
'
