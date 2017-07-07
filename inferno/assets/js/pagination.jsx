var React = require('react')

const Pagination = (props) => {
  let school = props.items.school,
      ctype  = props.items.ctype,
      length = props.items.TotalPage;
  let querystring = (new URL(location)).searchParams;
  let startID = querystring.get('start')
  let start = (querystring.get('start')-1)/10+1
  let end = start + 11 < length ? start + 11 : length
  const turnLeft = (event) => {
    window.location.href = `/infernoWeb/sloth?school=${school}&start=${parseInt(startID)-10}&ctype=${ctype}`
  }
  const turnRight = (event) => {
    window.location.href = `/infernoWeb/sloth?school=${school}&start=${parseInt(startID)+10}&ctype=${ctype}`;

  }
  return(
    <div className="ui grid">
      <div className="three wide column"></div>
      <div className="ui borderless menu">
        <a className="item" id='turnleft' onClick={turnLeft}><i className="angle left icon"></i></a>
        {
          Array.from({length: end-(start-1)}, (v, k) => (k+start-1) ).map((item, index)=>{
            if(item+1==start){
              return <a key={index} className="item active" href={`/infernoWeb/sloth?school=${school}&start=${item*10+1}&ctype=${ctype}`}>{item+1}</a>
            }
            return <a key={index} className="item" href={`/infernoWeb/sloth?school=${school}&start=${item*10+1}&ctype=${ctype}`}>{item+1}</a>
          })
        }
        <a className="item" id='turnright' onClick={turnRight}><i className="angle right icon"></i></a>
      </div>          
    </div>
  )
}
export default  Pagination