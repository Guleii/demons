import zxing


"""
    二维码扫码识别
"""


def qr_code_scan(src_path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(src_path)
    return barcode.parsed