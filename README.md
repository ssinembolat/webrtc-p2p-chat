# WebRTC P2P Real-Time Video Communication System 📹✨

Bu proje, **Python Flask** ve **WebRTC API** kullanılarak geliştirilmiş, tarayıcılar arasında sunucu yükü olmadan doğrudan (**Peer-to-Peer**) ses ve görüntü iletimi sağlayan bir gerçek zamanlı iletişim sistemidir.

## 🚀 Özellikler
- **Uçtan Uca (P2P) İletişim:** Video ve ses verisi sunucuya uğramadan doğrudan eşler arasında aktarılır.
- **Asenkron Sinyalleşme:** Flask ve Socket.IO kullanılarak geliştirilmiş, düşük gecikmeli sinyalleşme katmanı.
- **NAT Traversal (STUN):** Google STUN sunucuları entegrasyonu ile modem ve güvenlik duvarı engellerini aşma.
- **Dinamik UI/UX:** Bağlantı kurulduğunda otomatik süzülen Picture-in-Picture (PiP) arayüz tasarımı.
- **Güvenli İletişim:** SRTP ve DTLS standartlarında uçtan uca şifreli medya akışı.

## 🛠️ Kullanılan Teknolojiler
- **Backend:** Python, Flask, Flask-SocketIO
- **Frontend:** JavaScript (Vanilla), WebRTC API, CSS3 (Flexbox/Grid)
- **Protokoller:** WebSocket, SDP, ICE, STUN

## 🏗️ Proje Mimarisi
Sistem üç ana aşamadan oluşmaktadır:
1. **Signaling (Sinyalleşme):** İstemciler Python sunucusu üzerinden teknik metadata (SDP Offer/Answer) takası yapar.
2. **Handshake (El Sıkışma):** ICE Candidates ile en uygun ağ rotası belirlenir.
3. **P2P Connection:** Bağlantı kurulduktan sonra medya akışı sunucudan bağımsız olarak doğrudan tarayıcılar arasında başlar.
