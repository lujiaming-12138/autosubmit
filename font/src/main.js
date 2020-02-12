// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Axios from 'axios'
import VueAxios from 'vue-axios'

Vue.config.productionTip = false
Vue.use(VueAxios, Axios)

/* eslint-disable no-new */
const v = new Vue({
  el: '#app',
  data: {
    location: ''
  },
  components: {App},
  template: '<App :location="location"/>'
})

window.onLoad = function () {
  const map = new AMap.Map('container', {
    resizeEnable: true
  })
  AMap.plugin('AMap.Geolocation', function () {
    const geolocation = new AMap.Geolocation({
      enableHighAccuracy: true,//是否使用高精度定位，默认:true
      timeout: 10000,          //超过10秒后停止定位，默认：5s
      buttonPosition: 'RB',    //定位按钮的停靠位置
      buttonOffset: new AMap.Pixel(10, 20),//定位按钮与设置的停靠位置的偏移量，默认：Pixel(10, 20)
      zoomToAccuracy: true,   //定位成功后是否自动调整地图视野到定位点
    })
    map.addControl(geolocation)
    geolocation.getCurrentPosition(function (status, result) {
      if (status == 'complete') {
        onComplete(result)
      } else {
        onError(result)
      }
    })
  })

  //解析定位结果
  function onComplete(data) {
    console.log('定位成功')
    console.log(JSON.stringify(data))
    let y = confirm(`确认位置\n${data.formattedAddress}`)
    if(y) {
      v.$data.location = JSON.stringify(data)
    }
  }

  //解析定位错误信息
  function onError(data) {
    alert('定位失败')
  }
}
const url = 'https://webapi.amap.com/maps?v=1.4.15&key=3b92304830e768aebb8bc8f6f9d49e87&callback=onLoad'
const jsapi = document.createElement('script')
jsapi.charset = 'utf-8'
jsapi.src = url
document.head.appendChild(jsapi)
