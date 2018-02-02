import qrcode


class QrCode:
    def generate_qr(data: str, file_path: str):
        """
        :type data:str
        :type file_path: str
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        with open(file_path, 'wb') as output:
            img.save(output)
            output.close()
