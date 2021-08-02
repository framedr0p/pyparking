from http.server import BaseHTTPRequestHandler, HTTPServer

# Hier wird die Adresse des Controller Servers definiert
server_address_httpd = ('10.10.0.6',80)

# Variabeln für die ID's der Parkplätze
p1 = 101
p2 = 102
p3 = 103
p4 = 104
p5 = 105
p6 = 106
p7 = 107
p8 = 108
p9 = 109
p10 = 110
p11 = 111
p12 = 112
p13 = 113
p14 = 114
p15 = 115
p16 = 116
p17 = 117
p18 = 118
p19 = 119
p20 = 120
p21 = 121
p22 = 122
p23 = 123
p24 = 124
p25 = 125
p26 = 126
p27 = 127
p28 = 128
p29 = 129
p30 = 130
p31 = 131
p32 = 132
p33 = 133
p34 = 134
p35 = 135

# Variablen für den Status jedes Parkplatzes
p1_status = 0
p2_status = 0
p3_status = 0
p4_status = 0
p5_status = 0
p6_status = 0
p7_status = 0
p8_status = 0
p9_status = 0
p10_status = 0
p11_status = 0
p12_status = 0
p13_status = 0
p14_status = 0
p15_status = 0
p16_status = 0
p17_status = 0
p18_status = 0
p19_status = 0
p20_status = 0
p21_status = 0
p22_status = 0
p23_status = 0
p24_status = 0
p25_status = 0
p26_status = 0
p27_status = 0
p28_status = 0
p29_status = 0
p30_status = 0
p31_status = 0
p32_status = 0
p33_status = 0
p34_status = 0
p35_status = 0

# zwei weitere Variabeln zum berechnen
summe= 0
slotID = None

# Hier wird die Funktion für die Verarbeiteung der Daten von den Sensoren erstellt - In global müssen die zu verwendenden Variabeln eingebunden werden!
class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global slotID, summe, p1, p1_status, p2, p2_status, p3, p3_status, p4, p4_status, p5, p5_status, p6, p6_status, p7, p7_status, p8, p8_status, p9, p9_status, p10, p10_status, p11, p11_status, p12, p12_status, p13, p13_status, p14, p14_status, p15, p15_status, p16, p16_status, p17, p17_status, p18, p18_status, p19, p19_status, p20, p20_status, p21, p21_status, p22, p22_status, p23, p23_status, p24, p24_status, p25, p25_status, p26, p26_status, p27, p27_status, p28, p28_status, p29, p29_status, p30, p30_status, p31, p31_status, p32, p32_status, p33, p33_status, p34, p34_status, p35, p35_status
    messagetosend = bytes('Welcome to Controller1',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    slotID = self.requestline
    print('incoming message:')
    print(slotID)
    
    # hier wird der Text der Anfrage gekürzt:
    slotID = slotID[5 : int(len(slotID)-9)]
    slotID = int(slotID)
    
    # das ist die IF schleife bei der festgestellt wird welche ID der Sensor hat und was er meldet
    if slotID > 1000:
        slotID = slotID - 1000
        if slotID == p1:
            p1_status = 1
        elif slotID == p2:
            p2_status = 1
        elif slotID == p3:
            p3_status = 1
        elif slotID == p4:
            p4_status = 1
        elif slotID == p5:
            p5_status = 1
        elif slotID == p6:
            p6_status = 1
        elif slotID == p7:
            p7_status = 1
        elif slotID == p8:
            p8_status = 1
        elif slotID == p9:
            p9_status = 1
        elif slotID == p10:
            p10_status = 1
        elif slotID == p11:
            p11_status = 1
        elif slotID == p12:
            p12_status = 1
        elif slotID == p13:
            p13_status = 1
        elif slotID == p14:
            p14_status = 1
        elif slotID == p15:
            p15_status = 1
        elif slotID == p16:
            p16_status = 1
        elif slotID == p17:
            p17_status = 1
        elif slotID == p18:
            p18_status = 1
        elif slotID == p19:
            p19_status = 1
        elif slotID == p20:
            p20_status = 1
        elif slotID == p21:
            p21_status = 1
        elif slotID == p22:
            p22_status = 1
        elif slotID == p23:
            p23_status = 1
        elif slotID == p24:
            p24_status = 1
        elif slotID == p25:
            p25_status = 1
        elif slotID == p26:
            p26_status = 1
        elif slotID == p27:
            p27_status = 1
        elif slotID == p28:
            p28_status = 1
        elif slotID == p29:
            p29_status = 1
        elif slotID == p30:
            p30_status = 1
        elif slotID == p31:
            p31_status = 1
        elif slotID == p32:
            p32_status = 1
        elif slotID == p33:
            p33_status = 1
        elif slotID == p34:
            p34_status = 1
        elif slotID == p35:
            p35_status = 1
    else:
        if slotID == p1:
            p1_status = 0
        elif slotID == p2:
            p2_status = 0
        elif slotID == p3:
            p3_status = 0
        elif slotID == p4:
            p4_status = 0
        elif slotID == p5:
            p5_status = 0
        elif slotID == p6:
            p6_status = 0
        elif slotID == p7:
            p7_status = 0
        elif slotID == p8:
            p8_status = 0
        elif slotID == p9:
            p9_status = 0
        elif slotID == p10:
            p10_status = 0
        elif slotID == p11:
            p11_status = 0
        elif slotID == p12:
            p12_status = 0
        elif slotID == p13:
            p13_status = 0
        elif slotID == p14:
            p14_status = 0
        elif slotID == p15:
            p15_status = 0
        elif slotID == p16:
            p16_status = 0
        elif slotID == p17:
            p17_status = 0
        elif slotID == p18:
            p18_status = 0
        elif slotID == p19:
            p19_status = 0
        elif slotID == p20:
            p20_status = 0
        elif slotID == p21:
            p21_status = 0
        elif slotID == p22:
            p22_status = 0
        elif slotID == p23:
            p23_status = 0
        elif slotID == p24:
            p24_status = 0
        elif slotID == p25:
            p25_status = 0
        elif slotID == p26:
            p26_status = 0
        elif slotID == p27:
            p27_status = 0
        elif slotID == p28:
            p28_status = 0
        elif slotID == p29:
            p29_status = 0
        elif slotID == p30:
            p30_status = 0
        elif slotID == p31:
            p31_status = 0
        elif slotID == p32:
            p32_status = 0
        elif slotID == p33:
            p33_status = 0
        elif slotID == p34:
            p34_status = 0
        elif slotID == p35:
            p35_status = 0
    
    # hier wird die Summe der FREIEN Parkplätze errechnet
    summe = p1_status + p2_status + p3_status + p4_status + p5_status + p6_status + p7_status + p8_status + p9_status + p10_status + p11_status + p12_status + p13_status + p14_status + p15_status + p16_status + p17_status + p18_status + p19_status + p20_status + p21_status + p22_status + p23_status + p24_status + p25_status + p26_status + p27_status + p28_status + p29_status + p30_status + p31_status + p32_status + p33_status + p34_status + p35_status
    
    # ab hier muss noch weiter gearbeitet werden um die Daten an das Display zu übergeben!
    print(summe)
    
    return

print('Starting server ...')
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
httpd.serve_forever()


