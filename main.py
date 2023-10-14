from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
# from streamlit_chat import message

# import os
# import yaml
# from streamlit_option_menu import option_menu
# from langchain.agents import create_json_agent, AgentExecutor
# from langchain.agents.agent_toolkits import JsonToolkit
# from langchain.chains import LLMChain
# from langchain.llms.openai import OpenAI
# from langchain.requests import TextRequestsWrapper
# from langchain.tools.json.tool import JsonSpec
import streamlit.components.v1 as com
# real_url = "http://localhost:8501/"
real_url = "https://professearch.streamlit.app/"
st.set_page_config(page_title="profesearch", page_icon=None, layout="wide", menu_items=None)#, initial_sidebar_state="collapsed"
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
    """
st.markdown(no_sidebar_style, unsafe_allow_html=True)
no_sidebar_style = """
    <style>
        section[data-testid="stSidebar"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

from streamlit_custom_notification_box import custom_notification_box
# st.subheader("Component with constant args")



# @st.cache_resource  # 👈 Add the caching decorator

# st.image(image="Toronto_1.png",use_column_width="auto")
# navbar = option_menu(
#     menu_title=None,
#     options= ["browse ai" , "table" , "about"],
#     icons=  ["robot" , "table", "book"],
#     menu_icon="cast",
#     orientation="horizontal",
#     default_index=0,

#                 )


# main_html = f"""
# <html>
#     <head>
#         <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
#         <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
#         <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
#     </head>
#     <body>
#         <div class="header-banner">
#             <h1 style="color: rgb(62, 219, 209);">profesearch</h1>
#         </div>
#         <div class="clear"></div>
#         <nav>
#             <div class="site-title">Finland</div>
#             <ul>
#                 <li><a href="{real_url}pricing?unknown?" target = "_self"  >Pricing</a></li>
#                 <li><a href="/events">Events</a></li>
#                 <li><a href="/contact">Contact</a></li>
#             <ul>
#         </nav>
#         <script>
#             $(window).scroll(function(){{
#             if ($(window).scrollTop() >= 300) {{
#                 $('nav').addClass('fixed-header');
#                 $('nav div').addClass('visible-title');
#             }}
#             else {{
#                 $('nav').removeClass('fixed-header');
#                 $('nav div').removeClass('visible-title');
#             }}
#         }});
#         </script>
#     </body>
# </html>
# """
style_css = """
header.css-18ni7ap.ezrtsby2{
    visibility: hidden;

}
div.block-container.css-z5fcl4.ea3mdgi4
{
    padding: 0px;
}
body { margin:0px; padding:0px; }
footer{
    
        padding-top: 0px;
        padding-bottom: 0px;
        height: 0px;
        visibility: hidden;
    }
"""
# style_css = """
# header.css-18ni7ap.ezrtsby2{
#     visibility: hidden;

# }

# div.block-container.css-z5fcl4.ea3mdgi4
# {
#     padding-top: 0px;
#     padding-left: 0px;
#     padding-right: 0px;

# }
# /* resets */
# body { margin:0px; padding:0px; }

# /* main */
# header {
#     height: 360px;
#     z-index: 10;
# }
# .header-banner {
#     background-color: #7888d3;
#     background-image: url('https://www.utsc.utoronto.ca/hr/sites/utsc.utoronto.ca.hr/files/styles/3_1_full_width_banner/public/images/page/UofT7685_20140909_UTSCStudentsWalktoClass_9902-lpr.jpeg?h=9df75cb1&itok=bG9DYg6R');
#     background-position: center;
#     background-repeat: no-repeat;
#     background-size: cover;
#     width: 100%;
#     height: 300px;
# }
# .header-banner h1{

# }
# header h1 {
#     background-color: rgba(18,72,120, 0.8);
#     color: #fff;
#     padding: 0 1rem;
#     position: absolute;
#     top: 2rem; 
#     left: 2rem;
# }

# .fixed-header {
#     position: fixed;
#     top: 0;
#     left: 0;
#     width: 100%; 
# }

# nav {
#     width: 100%;
#     height: 60px;
#     background: #292f36;
#     postion: fixed;
#     z-index: 10;
# }

# nav div {
#     color: white;
#     font-size: 2rem;
#     line-height: 60px;
#     position: absolute;
#     top: 0;
#     left: 2%;
#     visibility: hidden;
# }
# .visible-title {
#     visibility: visible;
# }

# nav ul { 
#     list-style-type: none;
#     margin: 0 2% auto 0;
#     padding-left: 0;
#     text-align: right;
#     max-width: 100%;
# }
# nav ul li { 
#     display: inline-block; 
#     line-height: 60px;
#     margin-left: 10px;
# }
# nav ul li a {
#     text-decoration: none; 
#     color: #a9abae;
# }

# /* demo content */
# body { 
#     color: #292f36;
#     font-family: helvetica;
#     line-height: 1.6;
# }
# .content{ 
#     margin: 0 auto;
#     padding: 4rem 0;
#     width: 960px;
#     max-width: 100%;
# }
# article {
#     float: left;
#     width: 720px;
# }
# article p:first-of-type {
#     margin-top: 0;
# }
# aside {
#     float: right;
#     width: 120px;
# }
# p img {
#     max-width: 100%;
# }

# @media only screen and (max-width: 960px) {
#     .content{ 
#         padding: 2rem 0;
#     }
#     article {
#         float: none;
#         margin: 0 auto;
#         width: 96%;
#     }
#     article:last-of-type {  
#         margin-bottom: 3rem;
#     }
#     aside {  
#         float: none;
#         text-align: center;
#         width: 100%;
#     }
# }
# """




# main_html = """
#         <head>
#             <script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
#             <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
#             <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.min.js"></script>
#         </head>

#     <nav class="navbar navbar-expand-custom navbar-mainbg">
#         <a class="navbar-brand navbar-logo" href="#">Navbar</a>
#         <button class="navbar-toggler" type="button" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
#         <i class="fas fa-bars text-white"></i>
#         </button>
#         <div class="collapse navbar-collapse" id="navbarSupportedContent">
#             <ul class="navbar-nav ml-auto">
#                 <div class="hori-selector"><div class="left"></div><div class="right"></div></div>
#                 <li class="nav-item">
#                     <a class="nav-link" href="javascript:void(0);"><i class="fas fa-tachometer-alt"></i>Dashboard</a>
#                 </li>
#                 <li class="nav-item active">
#                     <a class="nav-link" href="javascript:void(0);"><i class="far fa-address-book"></i>Address Book</a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link" href="javascript:void(0);"><i class="far fa-clone"></i>Components</a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link" href="javascript:void(0);"><i class="far fa-calendar-alt"></i>Calendar</a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link" href="javascript:void(0);"><i class="far fa-chart-bar"></i>Charts</a>
#                 </li>
#                 <li class="nav-item">
#                     <a class="nav-link" href="javascript:void(0);"><i class="far fa-copy"></i>Documents</a>
#                 </li>
#             </ul>
#         </div>
#     </nav>

#     <script>
#             // ---------Responsive-navbar-active-animation-----------
#         function test(){
#             var tabsNewAnim = $('#navbarSupportedContent');
#             var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
#             var activeItemNewAnim = tabsNewAnim.find('.active');
#             var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
#             var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
#             var itemPosNewAnimTop = activeItemNewAnim.position();
#             var itemPosNewAnimLeft = activeItemNewAnim.position();
#             $(".hori-selector").css({
#                 "top":itemPosNewAnimTop.top + "px", 
#                 "left":itemPosNewAnimLeft.left + "px",
#                 "height": activeWidthNewAnimHeight + "px",
#                 "width": activeWidthNewAnimWidth + "px"
#             });
#             $("#navbarSupportedContent").on("click","li",function(e){
#                 $('#navbarSupportedContent ul li').removeClass("active");
#                 $(this).addClass('active');
#                 var activeWidthNewAnimHeight = $(this).innerHeight();
#                 var activeWidthNewAnimWidth = $(this).innerWidth();
#                 var itemPosNewAnimTop = $(this).position();
#                 var itemPosNewAnimLeft = $(this).position();
#                 $(".hori-selector").css({
#                     "top":itemPosNewAnimTop.top + "px", 
#                     "left":itemPosNewAnimLeft.left + "px",
#                     "height": activeWidthNewAnimHeight + "px",
#                     "width": activeWidthNewAnimWidth + "px"
#                 });
#             });
#         }
#         $(document).ready(function(){
#             setTimeout(function(){ test(); });
#         });
#         $(window).on('resize', function(){
#             setTimeout(function(){ test(); }, 500);
#         });
#         $(".navbar-toggler").click(function(){
#             $(".navbar-collapse").slideToggle(300);
#             setTimeout(function(){ test(); });
#         });



#         // --------------add active class-on another-page move----------
#         jQuery(document).ready(function($){
#             // Get current path and find target link
#             var path = window.location.pathname.split("/").pop();

#             // Account for home page with empty path
#             if ( path == '' ) {
#                 path = 'index.html';
#             }

#             var target = $('#navbarSupportedContent ul li a[href="'+path+'"]');
#             // Add active class to target link
#             target.parent().addClass('active');
#         });




#         // Add active class on another page linked
#         // ==========================================
#         // $(window).on('load',function () {
#         //     var current = location.pathname;
#         //     console.log(current);
#         //     $('#navbarSupportedContent ul li a').each(function(){
#         //         var $this = $(this);
#         //         // if the current path is like this link, make it active
#         //         if($this.attr('href').indexOf(current) !== -1){
#         //             $this.parent().addClass('active');
#         //             $this.parents('.menu-submenu').addClass('show-dropdown');
#         //             $this.parents('.menu-submenu').parent().addClass('active');
#         //         }else{
#         //             $this.parent().removeClass('active');
#         //         }
#         //     })
#         // });
#     </script>
#     """

# style_css = """
# @import url('https://fonts.googleapis.com/css?family=Roboto');

# header.css-18ni7ap.ezrtsby2{
#     visibility: hidden;

# }
# .navbar navbar-expand-custom navbar-mainbg{
#     position: fixed;
#     width: 100%;
#     top: 0;
#     left: 0;
#     color: white;
#     font-family: 'Exo 2', sans-serif;
#     padding: 1em;
# }
# div.block-container.css-z5fcl4.ea3mdgi4
# {
#     padding-top: 0px;
#     padding-left: 0px;
#     padding-right: 0px;

# }
# body{
# 	font-family: 'Roboto', sans-serif;
# }
# * {
# 	margin: 0;
# 	padding: 0;
# }
# i {
# 	margin-right: 10px;
# }
# /*----------bootstrap-navbar-css------------*/
# .navbar-logo{
# 	padding: 15px;
# 	color: #fff;
# }
# .navbar-mainbg{
# 	background-color: #5161ce;
# 	padding: 0px;
# }
# #navbarSupportedContent{
# 	overflow: hidden;
# 	position: relative;
# }
# #navbarSupportedContent ul{
# 	padding: 0px;
# 	margin: 0px;
# }
# #navbarSupportedContent ul li a i{
# 	margin-right: 10px;
# }
# #navbarSupportedContent li {
# 	list-style-type: none;
# 	float: left;
# }
# #navbarSupportedContent ul li a{
# 	color: rgba(255,255,255,0.5);
#     text-decoration: none;
#     font-size: 15px;
#     display: block;
#     padding: 20px 20px;
#     transition-duration:0.6s;
# 	transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
#     position: relative;
# }
# #navbarSupportedContent>ul>li.active>a{
# 	color: #5161ce;
# 	background-color: transparent;
# 	transition: all 0.7s;
# }
# #navbarSupportedContent a:not(:only-child):after {
# 	content: "\f105";
# 	position: absolute;
# 	right: 20px;
# 	top: 10px;
# 	font-size: 14px;
# 	font-family: "Font Awesome 5 Free";
# 	display: inline-block;
# 	padding-right: 3px;
# 	vertical-align: middle;
# 	font-weight: 900;
# 	transition: 0.5s;
# }
# #navbarSupportedContent .active>a:not(:only-child):after {
# 	transform: rotate(90deg);
# }
# .hori-selector{
# 	display:inline-block;
# 	position:absolute;
# 	height: 100%;
# 	top: 0px;
# 	left: 0px;
# 	transition-duration:0.6s;
# 	transition-timing-function: cubic-bezier(0.68, -0.55, 0.265, 1.55);
# 	background-color: #fff;
# 	border-top-left-radius: 15px;
# 	border-top-right-radius: 15px;
# 	margin-top: 10px;
# }
# .hori-selector .right,
# .hori-selector .left{
# 	position: absolute;
# 	width: 25px;
# 	height: 25px;
# 	background-color: #fff;
# 	bottom: 10px;
# }
# .hori-selector .right{
# 	right: -25px;
# }
# .hori-selector .left{
# 	left: -25px;
# }
# .hori-selector .right:before,
# .hori-selector .left:before{
# 	content: '';
#     position: absolute;
#     width: 50px;
#     height: 50px;
#     border-radius: 50%;
#     background-color: #5161ce;
# }
# .hori-selector .right:before{
# 	bottom: 0;
#     right: -25px;
# }
# .hori-selector .left:before{
# 	bottom: 0;
#     left: -25px;
# }


# @media(min-width: 992px){
# 	.navbar-expand-custom {
# 	    -ms-flex-flow: row nowrap;
# 	    flex-flow: row nowrap;
# 	    -ms-flex-pack: start;
# 	    justify-content: flex-start;
# 	}
# 	.navbar-expand-custom .navbar-nav {
# 	    -ms-flex-direction: row;
# 	    flex-direction: row;
# 	}
# 	.navbar-expand-custom .navbar-toggler {
# 	    display: none;
# 	}
# 	.navbar-expand-custom .navbar-collapse {
# 	    display: -ms-flexbox!important;
# 	    display: flex!important;
# 	    -ms-flex-preferred-size: auto;
# 	    flex-basis: auto;
# 	}
# }


# @media (max-width: 991px){
# 	#navbarSupportedContent ul li a{
# 		padding: 12px 30px;
# 	}
# 	.hori-selector{
# 		margin-top: 0px;
# 		margin-left: 10px;
# 		border-radius: 0;
# 		border-top-left-radius: 25px;
# 		border-bottom-left-radius: 25px;
# 	}
# 	.hori-selector .left,
# 	.hori-selector .right{
# 		right: 10px;
# 	}
# 	.hori-selector .left{
# 		top: -25px;
# 		left: auto;
# 	}
# 	.hori-selector .right{
# 		bottom: -25px;
# 	}
# 	.hori-selector .left:before{
# 		left: -25px;
# 		top: -25px;
# 	}
# 	.hori-selector .right:before{
# 		bottom: -25px;
# 		left: -25px;
# 	}
# }"""

# main_html = """
# <head>
#     <script src="https://raw.githubusercontent.com/IronSummitMedia/startbootstrap/gh-pages/templates/agency/js/jquery-1.11.0.js"></script>
#     <!-- Bootstrap Core JavaScript -->
#     <script src="https://raw.githubusercontent.com/IronSummitMedia/startbootstrap/gh-pages/templates/agency/js/bootstrap.min.js"></script>
#     <!-- Plugin JavaScript -->
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js"></script>
#     <script src="https://raw.githubusercontent.com/IronSummitMedia/startbootstrap/gh-pages/templates/agency/js/classie.js"></script>
#     <script src="https://raw.githubusercontent.com/IronSummitMedia/startbootstrap/gh-pages/templates/agency/js/cbpAnimatedHeader.js"></script>
#     <!-- Contact Form JavaScript -->
#     <script src="https://raw.githubusercontent.com/IronSummitMedia/startbootstrap/gh-pages/templates/agency/js/jqBootstrapValidation.js"></script>
#     <script src="https://raw.githubusercontent.com/IronSummitMedia/startbootstrap/gh-pages/templates/agency/js/contact_me.js"></script>
# </head>
# <body id="page-top" class="index" data-pinterest-extension-installed="cr1.3.4">
#     <!-- Navigation -->
#     <nav class="navbar navbar-default navbar-fixed-top navbar-shrink">
#         <div class="container">
#             <!-- Brand and toggle get grouped for better mobile display -->
#             <div class="navbar-header page-scroll">
#                 <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
#                     <span class="sr-only">Toggle navigation</span>
#                     <span class="icon-bar"></span>
#                     <span class="icon-bar"></span>
#                     <span class="icon-bar"></span>
#                 </button>
#                 <a class="navbar-brand page-scroll" href="#page-top">Celine Is Awesome</a>
#             </div>
#             <!-- Collect the nav links, forms, and other content for toggling -->
#             <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
#                 <ul class="nav navbar-nav navbar-right">
#                     <li class="hidden active">
#                         <a href="#page-top"></a>
#                     </li>
#                     <li class="">
#                         <a class="page-scroll" href="#services">Services</a>
#                     </li>
#                     <li class="">
#                         <a class="page-scroll" href="#portfolio">Portfolio</a>
#                     </li>
#                     <li class="">
#                         <a class="page-scroll" href="#about">About</a>
#                     </li>
#                     <li class="">
#                         <a class="page-scroll" href="#team">Team</a>
#                     </li>
#                     <li class="">
#                         <a class="page-scroll" href="#contact">Contact</a>
#                     </li>
#                 </ul>
#             </div>
#             <!-- /.navbar-collapse -->
#         </div>
#         <!-- /.container-fluid -->
#     </nav>
#     <!-- Header -->
#     <header>
#         <div class="container">
#             <div class="intro-text">
#                 <div class="intro-lead-in">Hello Errbody</div>
#                 <div class="intro-heading">Yes Mel, Ajmal, Chien, Junne maybe and Syok.</div>
#                 <a href="#services" class="page-scroll btn btn-xl">Aku Bukan Sempit</a>
#             </div>
#         </div>
#     </header>
#     <!-- Services Section -->
#     <section id="services">
#         <div class="container">
#             <div class="row">
#                 <div class="col-lg-12 text-center">
#                     <h2 class="section-heading">Services</h2>
#                     <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
#                 </div>
#             </div>
#             <div class="row text-center">
#                 <div class="col-md-4">
#                     <span class="fa-stack fa-4x">
#                         <i class="fa fa-circle fa-stack-2x text-primary"></i>
#                         <i class="glyphicon glyphicon-tree-conifer"></i>
#                     </span>
#                     <h4 class="service-heading">Here is a pokok</h4>
#                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.</p>
#                 </div>
#                 <div class="col-md-4">
#                     <span class="fa-stack fa-4x">
#                         <i class="fa fa-circle fa-stack-2x text-primary"></i>
#                         <i class="glyphicon glyphicon-heart"></i>
#                     </span>
#                     <h4 class="service-heading">Here's a heart</h4>
#                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.</p>
#                 </div>
#                 <div class="col-md-4">
#                     <span class="fa-stack fa-4x">
#                         <i class="fa fa-circle fa-stack-2x text-primary"></i>
#                         <i class="glyphicon glyphicon-tint"></i>
#                     </span>
#                     <h4 class="service-heading">Waterfall maybe?</h4>
#                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minima maxime quam architecto quo inventore harum ex magni, dicta impedit.</p>
#                 </div>
#             </div>
#         </div>
#     </section>
#     <!-- Portfolio Grid Section -->
#     <!-- About Section -->
#     <section id="about">
#         <div class="container">
#             <div class="row">
#                 <div class="col-lg-12 text-center">
#                     <h2 class="section-heading">About</h2>
#                     <h3 class="section-subheading text-muted">Ajmal, I need help to learn how to tweak this part. I don't want this timeline crap. Haha.</h3>
#                 </div>
#             </div>
#             <div class="row">
#                 <div class="col-lg-12">
#                     <ul class="timeline">
#                         <li>
#                             <div class="timeline-image">
#                                 <img class="img-circle img-responsive" src="img/about/1.jpg" alt="">
#                             </div>
#                             <div class="timeline-panel">
#                                 <div class="timeline-heading">
#                                     <h4>2009-2011</h4>
#                                     <h4 class="subheading">Our Humble Beginnings</h4>
#                                 </div>
#                                 <div class="timeline-body">
#                                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!</p>
#                                 </div>
#                             </div>
#                         </li>
#                         <li class="timeline-inverted">
#                             <div class="timeline-image">
#                                 <img class="img-circle img-responsive" src="img/about/2.jpg" alt="">
#                             </div>
#                             <div class="timeline-panel">
#                                 <div class="timeline-heading">
#                                     <h4>March 2011</h4>
#                                     <h4 class="subheading">An Agency is Born</h4>
#                                 </div>
#                                 <div class="timeline-body">
#                                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!</p>
#                                 </div>
#                             </div>
#                         </li>
#                         <li>
#                             <div class="timeline-image">
#                                 <img class="img-circle img-responsive" src="img/about/3.jpg" alt="">
#                             </div>
#                             <div class="timeline-panel">
#                                 <div class="timeline-heading">
#                                     <h4>December 2012</h4>
#                                     <h4 class="subheading">Transition to Full Service</h4>
#                                 </div>
#                                 <div class="timeline-body">
#                                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!</p>
#                                 </div>
#                             </div>
#                         </li>
#                         <li class="timeline-inverted">
#                             <div class="timeline-image">
#                                 <img class="img-circle img-responsive" src="img/about/4.jpg" alt="">
#                             </div>
#                             <div class="timeline-panel">
#                                 <div class="timeline-heading">
#                                     <h4>July 2014</h4>
#                                     <h4 class="subheading">Phase Two Expansion</h4>
#                                 </div>
#                                 <div class="timeline-body">
#                                     <p class="text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt ut voluptatum eius sapiente, totam reiciendis temporibus qui quibusdam, recusandae sit vero unde, sed, incidunt et ea quo dolore laudantium consectetur!</p>
#                                 </div>
#                             </div>
#                         </li>
#                         <li class="timeline-inverted">
#                             <div class="timeline-image">
#                                 <h4>Be Part
#                                     <br>Of Our
#                                     <br>Story!</h4>
#                             </div>
#                         </li>
#                     </ul>
#                 </div>
#             </div>
#         </div>
#     </section>
#     <!-- Team Section -->
#     <section id="team" class="bg-light-gray">
#         <div class="container">
#             <div class="row">
#                 <div class="col-lg-12 text-center">
#                     <h2 class="section-heading">Our Amazing Team</h2>
#                     <h3 class="section-subheading text-muted">Lorem ipsum dolor sit amet consectetur.</h3>
#                 </div>
#             </div>
#             <div class="row">
#                 <div class="col-sm-4">
#                     <div class="team-member">
#                         <img src="http://www.mycatspace.com/wp-content/uploads/2013/08/adopting-a-cat.jpg" class="img-responsive img-circle" alt="">
#                         <h4>Kay Garland</h4>
#                         <p class="text-muted">Lead Designer</p>
#                         <ul class="list-inline social-buttons">
#                             <li><a href="#"><i class="fa fa-twitter"></i></a>
#                             </li>
#                             <li><a href="#"><i class="fa fa-facebook"></i></a>
#                             </li>
#                             <li><a href="#"><i class="fa fa-linkedin"></i></a>
#                             </li>
#                         </ul>
#                     </div>
#                 </div>
#                 <div class="col-sm-4">
#                     <div class="team-member">
#                         <img src="http://www.mycatspace.com/wp-content/uploads/2013/08/adopting-a-cat.jpg" class="img-responsive img-circle" alt="">
#                         <h4>Larry Parker</h4>
#                         <p class="text-muted">Lead Marketer</p>
#                         <ul class="list-inline social-buttons">
#                             <li><a href="#"><i class="fa fa-twitter"></i></a>
#                             </li>
#                             <li><a href="#"><i class="fa fa-facebook"></i></a>
#                             </li>
#                             <li><a href="#"><i class="fa fa-linkedin"></i></a>
#                             </li>
#                         </ul>
#                     </div>
#                 </div>
#                 <div class="col-sm-4">
#                     <div class="team-member">
#                         <img src="http://www.mycatspace.com/wp-content/uploads/2013/08/adopting-a-cat.jpg" class="img-responsive img-circle" alt="">
#                         <h4>Diana Pertersen</h4>
#                         <p class="text-muted">Lead Developer</p>
#                         <ul class="list-inline social-buttons">
#                             <li><a href="#"><i class="fa fa-twitter"></i></a>
#                             </li>
#                             <li><a href="#"><i class="fa fa-facebook"></i></a>
#                             </li>
#                             <li><a href="#"><i class="fa fa-linkedin"></i></a>
#                             </li>
#                         </ul>
#                     </div>
#                 </div>
#             </div>
#             <div class="row">
#                 <div class="col-lg-8 col-lg-offset-2 text-center">
#                     <p class="large text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut eaque, laboriosam veritatis, quos non quis ad perspiciatis, totam corporis ea, alias ut unde.</p>
#                 </div>
#             </div>
#         </div>
#     </section>
#     <!-- Clients Aside -->
#     <footer>
#         <div class="container">
#             <div class="row">
#                 <div class="col-md-4">
#                     <span class="copyright">Copyright © Your Website 2014</span>
#                 </div>
#                 <div class="col-md-4">
#                     <ul class="list-inline social-buttons">
#                         <li><a href="#"><i class="fa fa-twitter"></i></a>
#                         </li>
#                         <li><a href="#"><i class="fa fa-facebook"></i></a>
#                         </li>
#                         <li><a href="#"><i class="fa fa-linkedin"></i></a>
#                         </li>
#                     </ul>
#                 </div>
#                 <div class="col-md-4">
#                     <ul class="list-inline quicklinks">
#                         <li><a href="#">Privacy Policy</a>
#                         </li>
#                         <li><a href="#">Terms of Use</a>
#                         </li>
#                     </ul>
#                 </div>
#             </div>
#         </div>
#     </footer>
#     <!-- Portfolio Modals -->
#     <!-- Use the modals below to showcase details about your portfolio projects! -->
#     <!-- Portfolio Modal 1 -->
#     <!-- jQuery Version 1.11.0 -->
    
#     <span style="height: 20px; width: 40px; min-height: 20px; min-width: 40px; position: absolute; opacity: 0.85; z-index: 8675309; display: none; cursor: pointer; background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAUCAYAAAD/Rn+7AAADU0lEQVR42s2WXUhTYRjHz0VEVPRFUGmtVEaFUZFhHxBhsotCU5JwBWEf1EWEEVHQx4UfFWYkFa2biPJiXbUta33OXFtuUXMzJ4bK3Nqay7m5NeZq6h/tPQ+xU20zugjOxR/+7/O8539+5znnwMtNTExwJtMb3L/fiLv3botCSmUjeCaejTOb39AiFothfHxcFIrHY8RksZjBsckJcOIRMfFsHD/SsbExUYpnI8DR0dGUGjSb0byhEJp5Uqg5CTSzc2CQleJbMEj9/ywBcGRkJEk9DQqouEVQT1sK444yWI9UonmTjGqauVLEIlHa9x8lAMbj8SSpp0rwKGMVvg8P46vbg0C7na8z8JsMcgHe7jlEa+edRhiLy8n/TUMfu6EvLElk+U0WtGwrTrdfAGQf5J8iiK4LVzDU28t8JtMSocf8E+l68myaNFXm/6rXslLK7ay5TOunuRvZWpJuvwAYjUaTpOIWoquuAZ219RTaxKYp9BbjycoN5FvL9qH9TBX5rvoGdJythvXYSTxdtRnWylO/ZdqrLsGwszzhWQ593z2KlAwCYCQSSZJ6ehZ0W7bD9VBLgN0NCqr3qR7R2rBrL3pu3Sb/7nDlz2uy6cG0OXk0GTbZXzNp8trsPAQdTj6frlWzN2DcXZGKQQAMh8NJ6rpyHe+PnkCr/CAFdZyvpfpjuvkifLF9wIt1Wwlo0OHie1RvWrKa93RjzfzliTzPKz3ltB0/Tevmwp14wGUgHAzSOoUEwFAolFaaBSuhnslPRkJexUJtZ6v5HtUeLswl33n1BgEY5fvhs9sJ3FAiT+QYyyvoAQJuD0KBAFRTJNAuz5/s3gJgMBhMJwrVFRThM5tY5zUF/A4X1f2fvQTRLCuBreoim0YmAbqNJryvPEXeeq46kaNdkQ/1HCncbJKPs9ZSv2VHGfWsZ2hfkhKAfr8/pdxWKx4wwD69PmVfNSOL+lr2w+gYqHpWDtXt1xQ8AMlWU0e1lqLd/APRHoP8AJqWrQG9gYxcPMsvSJUvAA4MDKTUJ7MZLaVy8v+qT21tcDx/OemePr0RTkNrur4A6PP5xCgBsL+/X4wiQDpuuVxOeL1eMYmYeDY6sOp0z+B0OuHxeEQhxkJMFosJiSO/UinOI/8Pc+l7KKArAT8AAAAASUVORK5CYII=);"></span>
# </body>
# """

# style_css = """

#         /*!
#     * Start Bootstrap - Agency Bootstrap Theme (https://startbootstrap.com)
#     * Code licensed under the Apache License v2.0.
#     * For details, see http://www.apache.org/licenses/LICENSE-2.0.
#     */
#     body {
#         overflow-x: hidden;
#         font-family: "Roboto Slab","Helvetica Neue",Helvetica,Arial,sans-serif;
#     }
#     .text-muted {
#         color: #777;
#     }
#     .text-primary {
#         color: #1ee2e7;
#     }
#     p {
#         font-size: 14px;
#         line-height: 1.75;
#     }
#     p.large {
#         font-size: 16px;
#     }
#     a,
#     a:hover,
#     a:focus,
#     a:active,
#     a.active {
#         outline: 0;
#     }
#     a {
#         color: #1ee2e7;
#     }
#     a:hover,
#     a:focus,
#     a:active,
#     a.active {
#         color: #17d0d5;
#     }
#     h1,
#     h2,
#     h3,
#     h4,
#     h5,
#     h6 {
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 700;
#     }
#     .img-centered {
#         margin: 0 auto;
#     }
#     .bg-light-gray {
#         background-color: #f7f7f7;
#     }
#     .bg-darkest-gray {
#         background-color: #222;
#     }
#     .btn-primary {
#         border-color: #1ee2e7;
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 700;
#         color: #fff;
#         background-color: #1ee2e7;
#     }
#     .btn-primary:hover,
#     .btn-primary:focus,
#     .btn-primary:active,
#     .btn-primary.active,
#     .open .dropdown-toggle.btn-primary {
#         border-color: #17d0d5;
#         color: #fff;
#         background-color: #17d0d5;
#     }
#     .btn-primary:active,
#     .btn-primary.active,
#     .open .dropdown-toggle.btn-primary {
#         background-image: none;
#     }
#     .btn-primary.disabled,
#     .btn-primary[disabled],
#     fieldset[disabled] .btn-primary,
#     .btn-primary.disabled:hover,
#     .btn-primary[disabled]:hover,
#     fieldset[disabled] .btn-primary:hover,
#     .btn-primary.disabled:focus,
#     .btn-primary[disabled]:focus,
#     fieldset[disabled] .btn-primary:focus,
#     .btn-primary.disabled:active,
#     .btn-primary[disabled]:active,
#     fieldset[disabled] .btn-primary:active,
#     .btn-primary.disabled.active,
#     .btn-primary[disabled].active,
#     fieldset[disabled] .btn-primary.active {
#         border-color: #1ee2e7;
#         background-color: #1ee2e7;
#     }
#     .btn-primary .badge {
#         color: #1ee2e7;
#         background-color: #fff;
#     }

#     .btn-xl {
#         padding: 20px 40px;
#         border-color: #1ee2e7;
#         border-radius: 3px;
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-size: 18px;
#         font-weight: 700;
#         color: #fff;
#         background-color: #1ee2e7;
#     }

#     .btn-xl:hover,
#     .btn-xl:focus,
#     .btn-xl:active,
#     .btn-xl.active,
#     .open .dropdown-toggle.btn-xl {
#         border-color: #17d0d5;
#         color: #fff;
#         background-color: #17d0d5;
#     }

#     .btn-xl:active,
#     .btn-xl.active,
#     .open .dropdown-toggle.btn-xl {
#         background-image: none;
#     }

#     .btn-xl.disabled,
#     .btn-xl[disabled],
#     fieldset[disabled] .btn-xl,
#     .btn-xl.disabled:hover,
#     .btn-xl[disabled]:hover,
#     fieldset[disabled] .btn-xl:hover,
#     .btn-xl.disabled:focus,
#     .btn-xl[disabled]:focus,
#     fieldset[disabled] .btn-xl:focus,
#     .btn-xl.disabled:active,
#     .btn-xl[disabled]:active,
#     fieldset[disabled] .btn-xl:active,
#     .btn-xl.disabled.active,
#     .btn-xl[disabled].active,
#     fieldset[disabled] .btn-xl.active {
#         border-color: #1ee2e7;
#         background-color: #1ee2e7;
#     }

#     .btn-xl .badge {
#         color: #fed136;
#         background-color: #fff;
#     }

#     .navbar-default {
#         border-color: transparent;
#         background-color: #222;
#     }

#     .navbar-default .navbar-brand {
#         font-family: "Kaushan Script","Helvetica Neue",Helvetica,Arial,cursive;
#         color: #1ee2e7;
#     }

#     .navbar-default .navbar-brand:hover,
#     .navbar-default .navbar-brand:focus,
#     .navbar-default .navbar-brand:active,
#     .navbar-default .navbar-brand.active {
#         color: #fec503;
#     }

#     .navbar-default .navbar-collapse {
#         border-color: rgba(255,255,255,.02);
#     }

#     .navbar-default .navbar-toggle {
#         border-color: #1ee2e7;
#         background-color: #1ee2e7;
#     }

#     .navbar-default .navbar-toggle .icon-bar {
#         background-color: #fff;
#     }

#     .navbar-default .navbar-toggle:hover,
#     .navbar-default .navbar-toggle:focus {
#         background-color: #1ee2e7;
#     }

#     .navbar-default .nav li a {
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 400;
#         letter-spacing: 1px;
#         color: #fff;
#     }

#     .navbar-default .nav li a:hover,
#     .navbar-default .nav li a:focus {
#         outline: 0;
#         color: #1ee2e7;
#     }

#     .navbar-default .navbar-nav>.active>a {
#         border-radius: 0;
#         color: #fff;
#         background-color: #1ee2e7;
#     }

#     .navbar-default .navbar-nav>.active>a:hover,
#     .navbar-default .navbar-nav>.active>a:focus {
#         color: #fff;
#         background-color: #17d0d5;
#     }

#     @media(min-width:768px) {
#         .navbar-default {
#             padding: 25px 0;
#             border: 0;
#             background-color: transparent;
#             -webkit-transition: padding .3s;
#             -moz-transition: padding .3s;
#             transition: padding .3s;
#         }

#         .navbar-default .navbar-brand {
#             font-size: 2em;
#             -webkit-transition: all .3s;
#             -moz-transition: all .3s;
#             transition: all .3s;
#         }

#         .navbar-default .navbar-nav>.active>a {
#             border-radius: 3px;
#         }

#         .navbar-default.navbar-shrink {
#             padding: 10px 0;
#             background-color: #222;
#         }

#         .navbar-default.navbar-shrink .navbar-brand {
#             font-size: 1.5em;
#         }
#     }

#     header {
#         text-align: center;
#         color: #fff;
#         background-attachment: scroll;
#         background-image: url(https://unsplash.imgix.net/uploads%2F14115408840644deb16b0%2F2dc933e3?q=75&fm=jpg&auto=format&s=7f43646e4d26049c6c39890afb2e5ced);
#         background-position: center center;
#         background-repeat: none;
#         -webkit-background-size: cover;
#         -moz-background-size: cover;
#         background-size: cover;
#         -o-background-size: cover;
#     }

#     header .intro-text {
#         padding-top: 100px;
#         padding-bottom: 50px;
#     }

#     header .intro-text .intro-lead-in {
#         margin-bottom: 25px;
#         font-family: "Droid Serif","Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-size: 22px;
#         font-style: italic;
#         line-height: 22px;
#     }

#     header .intro-text .intro-heading {
#         margin-bottom: 25px;
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-size: 50px;
#         font-weight: 700;
#         line-height: 50px;
#     }

#     @media(min-width:768px) {
#         header .intro-text {
#             padding-top: 300px;
#             padding-bottom: 200px;
#         }

#         header .intro-text .intro-lead-in {
#             margin-bottom: 25px;
#             font-family: "Droid Serif","Helvetica Neue",Helvetica,Arial,sans-serif;
#             font-size: 40px;
#             font-style: italic;
#             line-height: 40px;
#         }

#         header .intro-text .intro-heading {
#             margin-bottom: 50px;
#             text-transform: uppercase;
#             font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#             font-size: 75px;
#             font-weight: 700;
#             line-height: 75px;
#         }
#     }

#     section {
#         padding: 100px 0;
#     }

#     section h2.section-heading {
#         margin-top: 0;
#         margin-bottom: 15px;
#         font-size: 40px;
#     }

#     section h3.section-subheading {
#         margin-bottom: 75px;
#         text-transform: none;
#         font-family: "Droid Serif","Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-size: 16px;
#         font-style: italic;
#         font-weight: 400;
#     }

#     @media(min-width:768px) {
#         section {
#             padding: 150px 0;
#         }
#     }

#     .service-heading {
#         margin: 15px 0;
#         text-transform: none;
#     }

#     #portfolio .portfolio-item {
#         right: 0;
#         margin: 0 0 15px;
#     }

#     #portfolio .portfolio-item .portfolio-link {
#         display: block;
#         position: relative;
#         margin: 0 auto;
#         max-width: 400px;
#     }

#     #portfolio .portfolio-item .portfolio-link .portfolio-hover {
#         position: absolute;
#         width: 100%;
#         height: 100%;
#         opacity: 0;
#         background: #1ee2e7;
#         -webkit-transition: all ease .5s;
#         -moz-transition: all ease .5s;
#         transition: all ease .5s;
#     }

#     #portfolio .portfolio-item .portfolio-link .portfolio-hover:hover {
#         opacity: 1;
#     }

#     #portfolio .portfolio-item .portfolio-link .portfolio-hover .portfolio-hover-content {
#         position: absolute;
#         top: 50%;
#         width: 100%;
#         height: 20px;
#         margin-top: -12px;
#         text-align: center;
#         font-size: 20px;
#         color: #fff;
#     }

#     #portfolio .portfolio-item .portfolio-link .portfolio-hover .portfolio-hover-content i {
#         margin-top: -12px;
#     }

#     #portfolio .portfolio-item .portfolio-link .portfolio-hover .portfolio-hover-content h3,
#     #portfolio .portfolio-item .portfolio-link .portfolio-hover .portfolio-hover-content h4 {
#         margin: 0;
#     }

#     #portfolio .portfolio-item .portfolio-caption {
#         margin: 0 auto;
#         padding: 25px;
#         max-width: 400px;
#         text-align: center;
#         background-color: #fff;
#     }

#     #portfolio .portfolio-item .portfolio-caption h4 {
#         margin: 0;
#         text-transform: none;
#     }

#     #portfolio .portfolio-item .portfolio-caption p {
#         margin: 0;
#         font-family: "Droid Serif","Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-size: 16px;
#         font-style: italic;
#     }

#     #portfolio * {
#         z-index: 2;
#     }

#     @media(min-width:767px) {
#         #portfolio .portfolio-item {
#             margin: 0 0 30px;
#         }
#     }

#     .timeline {
#         position: relative;
#         padding: 0;
#         list-style: none;
#     }

#     .timeline:before {
#         content: "";
#         position: absolute;
#         top: 0;
#         bottom: 0;
#         left: 40px;
#         width: 2px;
#         margin-left: -1.5px;
#         background-color: #f1f1f1;
#     }

#     .timeline>li {
#         position: relative;
#         margin-bottom: 50px;
#         min-height: 50px;
#     }

#     .timeline>li:before,
#     .timeline>li:after {
#         content: " ";
#         display: table;
#     }

#     .timeline>li:after {
#         clear: both;
#     }

#     .timeline>li .timeline-panel {
#         float: right;
#         position: relative;
#         width: 100%;
#         padding: 0 20px 0 100px;
#         text-align: left;
#     }

#     .timeline>li .timeline-panel:before {
#         right: auto;
#         left: -15px;
#         border-right-width: 15px;
#         border-left-width: 0;
#     }

#     .timeline>li .timeline-panel:after {
#         right: auto;
#         left: -14px;
#         border-right-width: 14px;
#         border-left-width: 0;
#     }

#     .timeline>li .timeline-image {
#         z-index: 100;
#         position: absolute;
#         left: 0;
#         width: 80px;
#         height: 80px;
#         margin-left: 0;
#         border: 7px solid #f1f1f1;
#         border-radius: 100%;
#         text-align: center;
#         color: #fff;
#         background-color: #1ee2e7;
#     }

#     .timeline>li .timeline-image h4 {
#         margin-top: 12px;
#         font-size: 10px;
#         line-height: 14px;
#     }

#     .timeline>li.timeline-inverted>.timeline-panel {
#         float: right;
#         padding: 0 20px 0 100px;
#         text-align: left;
#     }

#     .timeline>li.timeline-inverted>.timeline-panel:before {
#         right: auto;
#         left: -15px;
#         border-right-width: 15px;
#         border-left-width: 0;
#     }

#     .timeline>li.timeline-inverted>.timeline-panel:after {
#         right: auto;
#         left: -14px;
#         border-right-width: 14px;
#         border-left-width: 0;
#     }

#     .timeline>li:last-child {
#         margin-bottom: 0;
#     }

#     .timeline .timeline-heading h4 {
#         margin-top: 0;
#         color: inherit;
#     }

#     .timeline .timeline-heading h4.subheading {
#         text-transform: none;
#     }

#     .timeline .timeline-body>p,
#     .timeline .timeline-body>ul {
#         margin-bottom: 0;
#     }

#     @media(min-width:768px) {
#         .timeline:before {
#             left: 50%;
#         }

#         .timeline>li {
#             margin-bottom: 100px;
#             min-height: 100px;
#         }

#         .timeline>li .timeline-panel {
#             float: left;
#             width: 41%;
#             padding: 0 20px 20px 30px;
#             text-align: right;
#         }

#         .timeline>li .timeline-image {
#             left: 50%;
#             width: 100px;
#             height: 100px;
#             margin-left: -50px;
#         }

#         .timeline>li .timeline-image h4 {
#             margin-top: 16px;
#             font-size: 13px;
#             line-height: 18px;
#         }

#         .timeline>li.timeline-inverted>.timeline-panel {
#             float: right;
#             padding: 0 30px 20px 20px;
#             text-align: left;
#         }
#     }

#     @media(min-width:992px) {
#         .timeline>li {
#             min-height: 150px;
#         }

#         .timeline>li .timeline-panel {
#             padding: 0 20px 20px;
#         }

#         .timeline>li .timeline-image {
#             width: 150px;
#             height: 150px;
#             margin-left: -75px;
#         }

#         .timeline>li .timeline-image h4 {
#             margin-top: 30px;
#             font-size: 18px;
#             line-height: 26px;
#         }

#         .timeline>li.timeline-inverted>.timeline-panel {
#             padding: 0 20px 20px;
#         }
#     }

#     @media(min-width:1200px) {
#         .timeline>li {
#             min-height: 170px;
#         }

#         .timeline>li .timeline-panel {
#             padding: 0 20px 20px 100px;
#         }

#         .timeline>li .timeline-image {
#             width: 170px;
#             height: 170px;
#             margin-left: -85px;
#         }

#         .timeline>li .timeline-image h4 {
#             margin-top: 40px;
#         }

#         .timeline>li.timeline-inverted>.timeline-panel {
#             padding: 0 100px 20px 20px;
#         }
#     }

#     .team-member {
#         margin-bottom: 50px;
#         text-align: center;
#     }

#     .team-member img {
#         margin: 0 auto;
#         border: 7px solid #fff;
#     }

#     .team-member h4 {
#         margin-top: 25px;
#         margin-bottom: 0;
#         text-transform: none;
#     }

#     .team-member p {
#         margin-top: 0;
#     }


#     section#contact {
#         background-color: #222;
#         background-image: url(https://unsplash.imgix.net/44/C3EWdWzT8imxs0fKeKoC_blackforrest.JPG?q=75&fm=jpg&auto=format&s=986aaa92169d4e97975fa66ebd60bafd);
#         background-position: center;
#         background-repeat: no-repeat;
#     }

#     section#contact .section-heading {
#         color: #fff;
#     }

#     section#contact .form-group {
#         margin-bottom: 25px;
#     }

#     section#contact .form-group input,
#     section#contact .form-group textarea {
#         padding: 20px;
#     }

#     section#contact .form-group input.form-control {
#         height: auto;
#     }

#     section#contact .form-group textarea.form-control {
#         height: 236px;
#     }

#     section#contact .form-control:focus {
#         border-color: #1ee2e7;
#         box-shadow: none;
#     }

#     section#contact::-webkit-input-placeholder {
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 700;
#         color: #bbb;
#     }

#     section#contact:-moz-placeholder {
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 700;
#         color: #bbb;
#     }

#     section#contact::-moz-placeholder {
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 700;
#         color: #bbb;
#     }

#     section#contact:-ms-input-placeholder {
#         text-transform: uppercase;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-weight: 700;
#         color: #bbb;
#     }

#     section#contact .text-danger {
#         color: #e74c3c;
#     }

#     footer {
#         padding: 25px 0;
#         text-align: center;
#     }

#     footer span.copyright {
#         text-transform: uppercase;
#         text-transform: none;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         line-height: 40px;
#     }

#     footer ul.quicklinks {
#         margin-bottom: 0;
#         text-transform: uppercase;
#         text-transform: none;
#         font-family: Montserrat,"Helvetica Neue",Helvetica,Arial,sans-serif;
#         line-height: 40px;
#     }

#     ul.social-buttons {
#         margin-bottom: 0;
#     }

#     ul.social-buttons li a {
#         display: block;
#         width: 40px;
#         height: 40px;
#         border-radius: 100%;
#         font-size: 20px;
#         line-height: 40px;
#         outline: 0;
#         color: #fff;
#         background-color: #222;
#         -webkit-transition: all .3s;
#         -moz-transition: all .3s;
#         transition: all .3s;
#     }

#     ul.social-buttons li a:hover,
#     ul.social-buttons li a:focus,
#     ul.social-buttons li a:active {
#         background-color: #1ee2e7;
#     }

#     .btn:focus,
#     .btn:active,
#     .btn.active,
#     .btn:active:focus {
#         outline: 0;
#     }

#     .portfolio-modal .modal-content {
#         padding: 100px 0;
#         min-height: 100%;
#         border: 0;
#         border-radius: 0;
#         text-align: center;
#         background-clip: border-box;
#         -webkit-box-shadow: none;
#         box-shadow: none;
#     }

#     .portfolio-modal .modal-content h2 {
#         margin-bottom: 15px;
#         font-size: 3em;
#     }

#     .portfolio-modal .modal-content p {
#         margin-bottom: 30px;
#     }

#     .portfolio-modal .modal-content p.item-intro {
#         margin: 20px 0 30px;
#         font-family: "Droid Serif","Helvetica Neue",Helvetica,Arial,sans-serif;
#         font-size: 16px;
#         font-style: italic;
#     }

#     .portfolio-modal .modal-content ul.list-inline {
#         margin-top: 0;
#         margin-bottom: 30px;
#     }

#     .portfolio-modal .modal-content img {
#         margin-bottom: 30px;
#     }

#     .portfolio-modal .close-modal {
#         position: absolute;
#         top: 25px;
#         right: 25px;
#         width: 75px;
#         height: 75px;
#         background-color: transparent;
#         cursor: pointer;
#     }

#     .portfolio-modal .close-modal:hover {
#         opacity: .3;
#     }

#     .portfolio-modal .close-modal .lr {
#         z-index: 1051;
#         width: 1px;
#         height: 75px;
#         margin-left: 35px;
#         background-color: #222;
#         -webkit-transform: rotate(45deg);
#         -ms-transform: rotate(45deg);
#         transform: rotate(45deg);
#     }

#     .portfolio-modal .close-modal .lr .rl {
#         z-index: 1052;
#         width: 1px;
#         height: 75px;
#         background-color: #222;
#         -webkit-transform: rotate(90deg);
#         -ms-transform: rotate(90deg);
#         transform: rotate(90deg);
#     }

#     ::-moz-selection {
#         text-shadow: none;
#         background: #1ee2e7;
#     }

#     ::selection {
#         text-shadow: none;
#         background: #1ee2e7;
#     }

#     img::selection {
#         background: 0 0;
#     }

#     img::-moz-selection {
#         background: 0 0;
#     }

#     body {
#         webkit-tap-highlight-color: #1ee2e7;
#     }

# """

# if navbar == "table":
# with open('index.html') as mainHTML:
#     com.html(mainHTML.read() ,height=360)

# com.html(main_html , height=360)

# Short description of the app
# some body
# set streamlit header z-index
st.markdown('''
<style>
.stApp header {
    z-index: 0;
}
</style>
''', unsafe_allow_html=True)

main_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.bundle.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University of Toronto Computer Science Professors</title>
    <style>
      .bg-cover {{
          background-size: cover !important;
      }}
      body {{
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          background-color: #f2f2f2;
      }}
      header {{
        background-color: #007acc;
        color: #fff;
        text-align: center;
      }}
      h1 {{
          font-size: 24px;
      }}
      main {{
          max-width: 800px;
          margin: 20px auto;
          padding: 20px;
          background-color: #fff;
          box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
      }}
      section {{
          margin-bottom: 20px;
      }}
      h2 {{
          font-size: 20px;
          color: #007acc;
          margin-bottom: 10px;
      }}
      main p {{
          font-size: 16px;
          line-height: 1.5;
          color: #333;
      }}
      label {{
          font-weight: bold;
      }}   
      #answer {{
          margin-top: 20px;
          font-weight: bold;
      }}
      .css-5rimss a {{
            color: rgb(255 255 255);
        }}
    </style>   
</head>
<body>
  <header>
      <nav class="navbar navbar-expand-lg navbar-dark " style="background-color: #007acc;position: fixed;top: 0px;width: 100%;z-index: 1000;">
        <div class="container-fluid">
          <a class="navbar-brand" href="#">
            <svg width="41" height="41" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md" role="img" style="width: 35px;height: 35px;margin-left: 1%;margin-right: 5%;"><text>ChatGPT</text>
            <path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg> 
            profesearch
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div class="navbar-nav">
              <a class="nav-link active" aria-current="page" href="{real_url}loginpage">login</a>
              <a class="nav-link" href="{real_url}pricing?unknown?" target = "_self">Pricing</a>
              <a class="nav-link disabled">about</a>
            </div>
          </div>
        </div>
      </nav>
      <div style="background: url(https://www.utsc.utoronto.ca/hr/sites/utsc.utoronto.ca.hr/files/styles/3_1_full_width_banner/public/images/page/UofT7685_20140909_UTSCStudentsWalktoClass_9902-lpr.jpeg?h=9df75cb1&itok=bG9DYg6R); border-radius: 0; " class="jumbotron bg-cover text-white" >
        <div class="container py-5 text-center">
          <br>
          <br><br>
            <h1 class="display-4 font-weight-bold">profesearch</h1>
            <p class="font-italic mb-0">Welcome to our website dedicated to providing information about computer engineering and computer science professors at the Universities of Canada.</p>
            <p>
            <a href="{real_url}pricing?unknown?" class="text-white" target = "_self" style="text-decoration: none;">
                <u style="text-decoration: none;">pricing</u>
            </a>
            </p>
            <a href="{real_url}loginpage" role="button" class="btn btn-primary px-5" >try free trial</a>
        </div>
      </div>
  </header>
    <main>
      <section>
        <h2>What Can We Do for You?</h2>
        <p>Welcome to our website dedicated to providing information about computer engineering and computer science professors at the University of Toronto. Our site is powered by advanced AI technology, which means you can ask us any question related to these fields, and we'll strive to provide you with accurate and informative answers.</p>
        <p>Whether you're a student looking for specific details about professors, their research, or their courses, contacts , or personal webpage we're here to help.</p>
        <p>Our AI-powered system is designed to assist you with:</p>
        <ul>
            <li>Exploring the profiles of computer science professors</li>
            <li>Discovering research areas and publications</li>
            <li>Understanding course offerings and syllabi</li>
            <li>Answering general questions related to computer engineering and computer science</li>
        </ul>
        <p>Just type your question and watch as our AI works its magic to provide you with the most relevant and up-to-date information available. We're your gateway to unlocking the vast world of computer science at the Universities of Canada.</p>
        <p>So, go ahead, start exploring, and feel free to ask us anything!</p>
        <div style="text-align: center;">
        <a href="{real_url}loginpage" role="button" class="btn btn-primary px-5">try free trial</a>
        </div>
    </section>
    </main>
    <script>
        // Add your GPT-3 integration code here to fetch and display answers
        // You'll need to make an API request to GPT-3 with the user's question and update the "answer" div with the response.
        // You should also handle any error cases and provide appropriate feedback to the user.
    </script>
</body>
</html>"""
st.markdown(main_html , unsafe_allow_html=True)

# with open("style.css") as style:
#     # com.html(f"<style>{style.read()}</style>" , height=0)
#      st.markdown(f"<style>{style.read()}</style>" , unsafe_allow_html=True)

st.markdown(f"<style>{style_css}</style>" , unsafe_allow_html=True)
# st.write("""
# # Chatbot ProfeSearch
         
# Connecting Graduate Students with Professors
# """)

# with open('main.html') as mainHTML:
#     com.html(mainHTML.read() , height=0)
# with open('main.html') as mainHTML:
#     st.markdown(style.read() , unsafe_allow_html=True)

# openai.api_key = st.secrets["a_key"]

# model = load_model()

# os.environ["OPENAI_API_KEY"] = st.secrets["a_key"]
 
     
# # #####################################################json
# with open("simpl_inf.yml") as f:
#     data = yaml.load(f, Loader=yaml.FullLoader)
# json_spec = JsonSpec(dict_=data, max_value_length=400)
# json_toolkit = JsonToolkit(spec=json_spec)

# json_agent_executor = create_json_agent(
#     llm=ChatOpenAI(model_name="text-babbage-001", openai_api_key= st.secrets["a_key"],max_tokens=100) #text-babbage-002
#     , toolkit=json_toolkit, verbose=True
# )

# # ######################################################



# # pinecone.init(api_key=st.secrets["pinecone_key"], environment='gcp-starter')
# # index = pinecone.Index('chatbot')

# index = pincone_intit_768()



# # st.header("prof")
        
# # st.subheader("Chatbot ProfeSearch \n Connecting Graduate Students with Professors")
# com.html( """<p>hear is a robot that can help you </p>""",width=260, height=50)
# if 'responses' not in st.session_state:
#     st.session_state['responses'] = ["How can I assist you?"]

# if 'requests' not in st.session_state:
#     st.session_state['requests'] = []

# llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key= st.secrets["a_key"])

# if 'buffer_memory' not in st.session_state:
#             st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)




# system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context, 
# and if the answer is not contained within the text below, say 'I don't know'""")


# human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

# prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

# conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

# from utils import *
def res(input):

    return f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <div class="card" style="background-color: #3f414d;padding-left: 13%;padding-right: 13%;color:white;">
    <div class="card-body">
        <div style="width: 35px;height: 35px;border-radius: 1px;background-color: #19c37d;color: white;">
            <svg width="41" height="41" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md" role="img" style="width: 35px;height: 30px;padding-top: 5px;"><text x="-9999" y="-9999">ChatGPT</text>
            <path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg>
        </div>
        <p style="color: white;margin-bottom: 0px;padding: 10px">{input}</p>
    </div>
    </div>
    <script>
     var paragraf = document.getElementsByTagName("p")
     paragraf.addClass("card-text")
     var h5_ = document.getElementsByTagName("h5")
     h5_.addClass("card-title")
    </script>
"""
def res_2(input):

    return f"""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <style>
        li p {{
            font-size: 22px; /* 1.5 times the parent font size */
            }}
        li::marker{{
            font-size: 20px;
        }}
        ol{{
            padding-left: 10px;
        }}
    </style>
    <div class="card" style="background-color: #3f414d;padding-left: 11%;padding-right: 11%;color:white;">
    <div class="card-body">
        <div style="width: 35px;height: 35px;border-radius: 1px;background-color: #19c37d;color: white;display: flex;">
            <svg width="41" height="41" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md" role="img" style="width: 35px;height: 30px;padding-top: 5px;"><text x="-9999" y="-9999">ChatGPT</text>
            <path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg>
        </div>
        <p style="color: white;margin-bottom: 0px;padding: 10px">{input}</p>
    </div>
    </div>
    <script>
    var paragraf = document.getElementsByTagName("p")
    paragraf.addClass("card-text")
    var h5_ = document.getElementsByTagName("h5")
    h5_.addClass("card-title")
    </script>
"""
# with st.form(key="query"):
#     question = st.subheader('write your question')
#     st.text_input("Query: ", key="input")
#     btn1, bt2, btn3, btn4, btn5 = st.columns(5)

#     with btn3:
#         send = st.form_submit_button('send' ,use_container_width=True)
# print(question)
# styles ={
#             'material-icons':{'color': 'red'},
#             'text-icon-link-close-container': {'box-shadow': '#3896de 0px 4px'}
#         }
# gpt = """Sure! Here is a list of professors specializing in machine learning along with their contact information, research interests, and website URLs:


# Please note that some professors may not have provided their website URLs."""

# message_placeholder = st.empty()
# full_response = ""
# for respons in gpt:# get_completion(prompt)
#     full_response += respons
#     message_placeholder.markdown(res(full_response + "▌"),unsafe_allow_html=True)
#     message_placeholder.markdown(res(full_response),unsafe_allow_html=True
# st.write("------")
# st.markdown(res(gpt),unsafe_allow_html=True)
# st.write("------")
# st.markdown(gpt)
# st.write("------")
# st.markdown(gpt,unsafe_allow_html=True)
# st.write("------")
# st.markdown(res_2(gpt),unsafe_allow_html=True)
# if send:  # #343541    #3f414d    #202123    #40414f    #1abc9c
#     if question:
#     # with st.spinner("typing..."):
#         custom_notification_box(icon='info', textDisplay='you must loging in', externalLink='login', url=f'{real_url}loginpage', styles=styles, key="foo")
        # st.warning("you must loging in")
        # st.markdown("""<a href="http://localhost:8501/loginpage"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
        # st.markdown("""<a href="https://emailverify.streamlit.app/table"   target = "_self"><button class="css-7ym5gk ef3psqc11"> login</button></a> """ , unsafe_allow_html=True)
# q = st.text_input("s")
# with st.chat_message("user"):
#     st.write(q)   
# with st.chat_message("users"):
#     st.write(q)  
# with st.chat_message("user"):
#     st.write(q)    
# query = st.text_input("Query: ", key="qury")
# if query:
#     with st.spinner("typing..."):
        
        # refined_query = query_refiner_2(query) # convert user query to a nice query
        # st.write(refined_query)
        # input_em = model.encode(refined_query).tolist()
        # input_em = model.encode(query).tolist()
        # result = find_match(refined_query)#index.query(input_em, top_k=6, includeMetadata=True)

        # result = find_match(query)
        # print("result" , result)


# #############################################################################################################cleaning data
        # for i in range(0 , len(result['matches'])):
        #     # result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace("\\n" ," ")
        #     # # result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace("https://" ,"")
        #     # result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace("page_url" ,"url")
        #     # result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace(", " ,",")
        #     # result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace(": " ,":")
        #     # result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace(". " ,".")


        #     if "{" in result['matches'][i]['metadata']['text']:
        #         if len(result['matches'][i]['metadata']['text'].split("{" , 1)[1]) > len(result['matches'][i]['metadata']['text'].split("{" , 1)[0]):
        #             result['matches'][i]['metadata']['text'] = "{"+result['matches'][i]['metadata']['text'].split("{" , 1)[1]
        #         else:
        #             result['matches'][i]['metadata']['text'] = "{"+result['matches'][i]['metadata']['text'].split("{" , 1)[0]
            
# ##########################################################################################################################
        # context = result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text'] 
        # context2 =result['matches'][2]['metadata']['text']+"\n"+result['matches'][3]['metadata']['text']
        # context3 =result['matches'][4]['metadata']['text']+"\n"+result['matches'][5]['metadata']['text']
        # print("context" , context)
        # response_json = json_agent_executor.run(query ) # json
        # print("json: ",response_json)
        # babbage_promt = f"""answer user request based Text.\nText:\n```{context2 + context3}``` \nuser request:```{refined_query}```"""

        # prompt = f"""your task is helping a user to find appropriate a list of professors interested in the specified research area . just anser based Text.\n\n Text:\n```{context}``` \n\n user request:\n ```{refined_query}```"""
        # babbage_response = get_completion(babbage_promt)
        # response = get_completion(prompt)
        #print(response)
        # st.markdown(res(response.choices[0].message["content"]), unsafe_allow_html=True)
        # st.markdown(res(context + "\n" + context2 + "\n" + context3), unsafe_allow_html=True)
        # st.markdown(res(response_json), unsafe_allow_html=True)
        
        # st.markdown(res(result), unsafe_allow_html=True)


# # container for chat history
# response_container = st.container()
# # container for text box
# textcontainer = st.container()


# with textcontainer:
#     s = st.text_area(label="Query:",key="text_area_key",height=2)
#     query = st.text_input("Query: ", key="input" )
#     if query:
#         with st.spinner("typing..."):
#             conversation_string = get_conversation_string()
#             # st.code(conversation_string)
#             refined_query = query_refiner(conversation_string, query) # convert user query to a nice query
#             st.subheader("Refined Query:")
#             st.write(refined_query)
#             print("refined" ,refined_query)

#             # context = find_match(refined_query)
#             input_em = model.encode(refined_query).tolist()
#             result = index.query(input_em, top_k=8, includeMetadata=True)
#             #############################################################################################################cleaning data
#             for i in range(0 , len(result['matches'])):
#                 result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace("\\n" ," ")
#                 result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace("https://" ,"")
#                 result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace("page_url" ,"url")
#                 result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace(", " ,",")
#                 result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace(": " ,":")
#                 result['matches'][i]['metadata']['text'] = result['matches'][i]['metadata']['text'].replace(". " ,".")


#                 if "{" in result['matches'][i]['metadata']['text']:
#                     if len(result['matches'][i]['metadata']['text'].split("{" , 1)[1]) > len(result['matches'][i]['metadata']['text'].split("{" , 1)[0]):
#                         result['matches'][i]['metadata']['text'] = "{"+result['matches'][i]['metadata']['text'].split("{" , 1)[1]
#                     else:
#                         result['matches'][i]['metadata']['text'] = "{"+result['matches'][i]['metadata']['text'].split("{" , 1)[0]
#             ##########################################################################################################################

#             context = result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']
#             context2 =result['matches'][2]['metadata']['text']+"\n"+result['matches'][3]['metadata']['text']
#             context3 = result['matches'][4]['metadata']['text']+"\n"+result['matches'][5]['metadata']['text']
#             context4 =result['matches'][6]['metadata']['text']+"\n"+result['matches'][7]['metadata']['text']

#             print("result" , result)
#             # print(context)  # sum of results
#             response1 = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{refined_query}") #convert response "the problem"
#             print("response1" , response1) 
#             response2 = conversation.predict(input=f"Context:\n {context2} \n\n Query:\n{refined_query}")
#             print("response2" , response2) 
#             response3 = conversation.predict(input=f"Context:\n {context3} \n\n Query:\n{refined_query}")
#             print("response3" , response3) 
#             response4 = conversation.predict(input=f"Context:\n {context4} \n\n Query:\n{refined_query}")
#             print("response4" , response4) 

#             # response5 = json_agent_executor.run(refined_query) # json
#             # print("response5" , response5) 

#             # response = conversation.predict(input=f"Context:\n {response1+response2+response3} \n\n Query:\n{query}")
#             prompt = f"""your task is helping a user to find appropriate professor . just anser based on provided Text.do not add  anything other than provided Text:\n```{response1+response2+response3 +response4 }``` \n\nuser request:\n ```{refined_query}```"""
#             response = get_completion(prompt)

#             # print("response" , response.choices[0].message["content"])  
        # st.session_state.requests.append(query)
#         st.session_state.responses.append(response.choices[0].message["content"]) 
        

# with response_container:
#     if st.session_state['responses']:

#         for i in range(len(st.session_state['responses'])):
#             message(st.session_state['responses'][i],key=str(i))
#             if i < len(st.session_state['requests']):
#                 message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')

          