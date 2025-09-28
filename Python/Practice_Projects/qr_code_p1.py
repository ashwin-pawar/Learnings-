import qrcode

#taking user upi id as input

upi_id = input("Enter Yoir UPI ID :-")

#upi id urls

phone_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url =f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'


#creating qr code

phone_pay_qr = qrcode.make(phone_pay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save qr image
phone_pay_qr.save('Phone_Pay.png')
google_pay_qr.save('Google_Pay.png')
paytm_qr.save('Paytm.png')

#showing the QR CODE on Display

phone_pay_qr.show()
##paytm_qr.show()

print("✅ QR Codes generated successfully!")