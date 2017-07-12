var React = require('react')
var ReactDOM = require('react-dom')
import Header from '../base/header.jsx'
import Footer from '../base/footer.jsx'
import Content from './content.jsx'

const Layout = (props) => (
  <div>
    <Header service={props.serviceName} school={props.school} urlpattern={props.urlpattern}/>
    <Content api='http://127.0.0.1:8000/sloth/get/clist?school=nchu&start=1'/>
    <Footer/>
  </div>
);



ReactDOM.render(
  <Layout serviceName='course' school='nchu' urlpattern='/infernoWeb/sloth/search'/>,
  document.getElementById('app')
);