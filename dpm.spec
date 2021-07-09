# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['dpm.py'],
             pathex=['/Users/derrick/.local/share/virtualenvs/package_manager-_W6B_IoJ/lib/python3.8/site-packages', '/Users/derrick/Documents/program/python/package_manager'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='dpm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
