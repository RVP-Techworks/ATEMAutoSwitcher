# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['switcher.py'],
    pathex=[],
    binaries=[],
    datas=[('graphics/icon.gif', 'graphics')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ATEMAutoSwitcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['graphics/icon.icns'],
)
app = BUNDLE(
    exe,
    name='ATEMAutoSwitcher.app',
    icon='graphics/icon.icns',
    bundle_identifier=None,
)
