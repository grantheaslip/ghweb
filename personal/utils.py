from whitenoise.storage import CompressedManifestStaticFilesStorage \
    as WhiteNoiseCompressedManifestStaticFilesStorage

class CompressedManifestStaticFilesStorage(
    WhiteNoiseCompressedManifestStaticFilesStorage
):
    def __init__(self, *args, **kwargs):
        self.patterns = tuple(self.patterns) + (
            ("*favicons/manifest.json", (
                (r'("src": "(.*)")', '"src": "%s"'),
            )),
            ("*favicons/browserconfig.xml", (
                (r'(src="(.*)")', 'src="%s"'),
            )),
        )
        super().__init__(*args, **kwargs)
