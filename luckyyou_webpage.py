import streamlit as st
import luckyyou
from datetime import date
# from Scripts.LuckyYou.luckyYouMain import twoSureNums

st.set_page_config(page_title="LuckyYou", page_icon="./luckyyou_icon_white.png", layout="wide", menu_items=None)

# Create a lucky you object
play = luckyyou.luckyYou()

st.header(":blue[LuckyYou]_:orange[!]_ :sunglasses:", divider=True)

col1, col2, col3 = st.columns(3, gap='medium')

with col1:
    st.text("The lucky numbers giver is here for you. Go ahead and try your luck!")
    st.write(":red[It's a simple process:] :orange[_Select the kind of numbers you want, and :blue[LuckyYou] gives you 10 different set of those numbers immedialtely_].")
    st.write("You can then go ahead and stake at your favourite joint. Goodluck!")

with col2:
    to_do = st.radio("What kind of numbers do you want to generate?", ["2-Sure", "Perm-5", "Nothing"], index=None)
    if to_do == "2-Sure":
        twoSureNums = play.twoSure()
        st.subheader("{} numbers :sparkles: :sparkles: :sparkles:".format(to_do), divider=True)
        for i in twoSureNums:
            num1, num2 = i.pop(), i.pop()
            st.metric(label="", value="{}, {}".format(num1, num2), label_visibility="collapsed", border=True, width="stretch")
        # st.balloons()
    elif to_do == "Perm-5":
        perm5Nums = play.perm5()
        st.subheader("{} numbers :fire: :fire: :fire: ".format(to_do), divider=True)
        for i in perm5Nums:
            num1, num2, num3, num4, num5 = i.pop(), i.pop(), i.pop(), i.pop(), i.pop()
            st.metric(label="", value="{}, {}, {}, {}, {}".format(num1, num2, num3, num4, num5), label_visibility="collapsed", border=True, width="stretch")
        # st.balloons()
    elif to_do == "Nothing":
        st.subheader("No numbers generated!", divider=True)
        st.write(":rainbow[It feels cold in here! There's nothing happening] :cloud:")
        # st.snow()


st.header("", divider="rainbow")
dt = date.today().year
# yr = dt.year
txt = "Wealth through numbers!"
st.info(" :copyright: Gershskills {}. {}".format(dt, txt))
# st.info(" :copyright: Gershskills {}".format(dt))
# st.info(txt)
st.write("Contact us:")
st.write(":email: gershskills@gmail.com")
st.write(":phone: 1(434) 922 2865, also for :violet[Telegram]")
