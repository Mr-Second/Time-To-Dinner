var React = require('react')
var ReactDOM = require('react-dom')

const Footer = () => {
  return(
    <footer className="ui blue inverted stackable container segment">
      <span>Copyright © 2016 All rights reserved.</span>
      <a target="_blank" href="https://www.facebook.com/CoursePickingHelper/"><i className="fa fa-facebook-square" aria-hidden="true"></i></a>
    </footer>
  );
}
export default  Footer;

ReactDOM.render(
  <Footer/>,
  document.getElementById('app')
);
