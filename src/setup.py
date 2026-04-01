from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.SF8VFDControl'
setup(name='enigma2-plugin-systemplugins-vfdcontrol',
       version='3.0',
       description='vfd controller',
       package_dir={pkg: 'SF8VFDControl'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
