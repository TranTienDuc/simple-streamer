import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration, RTCIceServer

# Cấu hình TURN và STUN
rtc_config = RTCConfiguration(
    iceServers=[
        RTCIceServer(urls=["stun:stun.l.google.com:19302"]),
        RTCIceServer(
            urls=["turn:openrelay.metered.ca:80"],
            username="openrelayproject",
            credential="openrelayproject"
        )
    ]
)

# Streamlit UI
st.title("💻 Streamlit WebRTC với TURN server")

webrtc_streamer(
    key="example",
    rtc_configuration=rtc_config,
    media_stream_constraints={"video": True, "audio": True},
)
