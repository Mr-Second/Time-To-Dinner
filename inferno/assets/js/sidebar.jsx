var React = require('react')

export default class SideBar extends React.Component{
  render(){
    const sidebarCatelog = ['通識', '必修', '選修', '其他'];
    return(
      <div className="two wide column">
        <div className="ui vertical menu" id="kind">
          {
            sidebarCatelog.map((item, idx) => (
              <a key={idx} className="item" href={"/infernoWeb/sloth?school=nchu&start=1&ctype="+item}>{item}</a>             
            ))
          }
        </div>
      </div>
    );
  }
}