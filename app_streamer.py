from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av

RTC_CONFIGURATION = RTCConfiguration(
    {
      "iceServers":[ 
        {'url': 'stun:global.stun.twilio.com:3478', 
         'urls': 'stun:global.stun.twilio.com:3478'
        }, 
        {'credential': '+AhWhqdmbiYjA/F2YuDkLhKm8CbxMTazACnzhUIT164=', 
         'url': 'turn:global.turn.twilio.com:3478?transport=udp', 
         'urls': 'turn:global.turn.twilio.com:3478?transport=udp', 
         'username': '5b29b713bcdbdf04d16795646c8d43304ac49e6b381f82778f3d8b0861b21c76'
        }, 
        {'credential': '+AhWhqdmbiYjA/F2YuDkLhKm8CbxMTazACnzhUIT164=', 
         'url': 'turn:global.turn.twilio.com:3478?transport=tcp', 
         'urls': 'turn:global.turn.twilio.com:3478?transport=tcp', 
         'username': '5b29b713bcdbdf04d16795646c8d43304ac49e6b381f82778f3d8b0861b21c76'
        }, 
        {'credential': '+AhWhqdmbiYjA/F2YuDkLhKm8CbxMTazACnzhUIT164=', 
         'url': 'turn:global.turn.twilio.com:443?transport=tcp', 
         'urls': 'turn:global.turn.twilio.com:443?transport=tcp', 
         'username': '5b29b713bcdbdf04d16795646c8d43304ac49e6b381f82778f3d8b0861b21c76'
        }
      ]
    }
)

class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")

webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)
