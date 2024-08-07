import streamlit as st

st.set_page_config(
     page_title="Web Absensi",
     page_icon="🗓️",
)

st.header(":mailbox: Info Lebih Lanjut")

st.write("Jika ada pertanyaan atau saran, silahkan isi formulir di bawah ini")

# Ganti 'XXXXXXXXXXXXXX' dengan ID formulir JotForm Anda
form_kontak = """
<iframe
    id="JotFormIFrame-242191427801452"
    title="JotForm Form"
    onload="window.parent.scrollTo(0,0)"
    allowtransparency="true"
    allowfullscreen="true"
    allow="geolocation; microphone; camera"
    src="https://form.jotform.com/242191427801452"
    frameborder="0"
    style="min-width:120%;height:1305px;border:none;"
    scrolling="no"
></iframe>
<script type="text/javascript">
    var ifr = document.getElementById("JotFormIFrame-242191427801452");
    if (ifr) {
        var src = ifr.src;
        var iframeParams = [];
        if (window.location.href && window.location.href.indexOf("?") > -1) {
            iframeParams = iframeParams.concat(window.location.href.substr(window.location.href.indexOf("?") + 1).split('&'));
        }
        if (src && src.indexOf("?") > -1) {
            iframeParams = iframeParams.concat(src.substr(src.indexOf("?") + 1).split("&"));
            src = src.substr(0, src.indexOf("?"));
        }
        iframeParams.push("isIframeEmbed=1");
        ifr.src = src + "?" + iframeParams.join('&');
    }
    window.handleIFrameMessage = function(e) {
        if (typeof e.data === 'object') { return; }
        var args = e.data.split(":");
        if (args.length > 2) { iframe = document.getElementById("JotFormIFrame-" + args[(args.length - 1)]); } 
        else { iframe = document.getElementById("JotFormIFrame"); }
        if (!iframe) { return; }
        switch (args[0]) {
            case "scrollIntoView":
                iframe.scrollIntoView();
                break;
            case "setHeight":
                iframe.style.height = args[1] + "px";
                break;
            case "collapseErrorPage":
                if (iframe.clientHeight > window.innerHeight) {
                    iframe.style.height = window.innerHeight + "px";
                }
                break;
            case "reloadPage":
                window.location.reload();
                break;
            case "loadScript":
                    if( typeof args[1] == 'string' && args[1].indexOf("http") === 0 && !e.origin.indexOf("jotform") ) {
                    var src = args[1].split("://")[1];
                    if (window.location.href.indexOf(src) > -1) { break; }
                    var script = document.createElement('script');
                    script.src = args[1];
                    script.type = "text/javascript";
                    document.body.appendChild(script);
                }
                break;
            case "exitFullscreen":
                if      (window.document.exitFullscreen)        window.document.exitFullscreen();
                else if (window.document.mozCancelFullScreen)   window.document.mozCancelFullScreen();
                else if (window.document.mozCancelFullscreen)   window.document.mozCancelFullScreen();
                else if (window.document.webkitExitFullscreen)  window.document.webkitExitFullscreen();
                else if (window.document.msExitFullscreen)      window.document.msExitFullscreen();
                break;
        }
        var isJotForm = (e.origin.indexOf("jotform") > -1) ? true : false;
        if(isJotForm && "contentWindow" in iframe && "postMessage" in iframe.contentWindow) {
            var urls = {"docurl":encodeURIComponent(document.URL),"referrer":encodeURIComponent(document.referrer)};
            iframe.contentWindow.postMessage(JSON.stringify({"type":"urls","value":urls}), "*");
        }
    };
    if (window.addEventListener) {
        window.addEventListener("message", handleIFrameMessage, false);
    } else if (window.attachEvent) {
        window.attachEvent("onmessage", handleIFrameMessage);
    }
</script>
"""

st.markdown(form_kontak, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("pages/model/style.css")
