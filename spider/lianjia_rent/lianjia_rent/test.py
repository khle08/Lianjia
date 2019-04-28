from bs4 import BeautifulSoup

html = """<div class="content__list">
                                 <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="145562" href="/apartment/15015.html"><img alt=" 冠寓 深圳景田国际公寓 商务开间 开间" src="https://image1.ljcdn.com/rent-user-avatar/681c1b18-4d61-4135-99e4-47f258e45949.250x182.jpg" data-src="https://image1.ljcdn.com/rent-user-avatar/681c1b18-4d61-4135-99e4-47f258e45949.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="145562" href="/apartment/15015.html">
                     冠寓 深圳景田国际公寓 商务开间 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                      <span class="room__left">仅剩 1 间</span>
                    <i> /</i>
                                    30㎡
                  <i>/</i> 南                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  冠寓                </p>
                                <p class="content__list--item--time oneline">10 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                </p>
                <span class="content__list--item-price"><em> 5200</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2215643257428787200.html"><img alt="  现代城华庭 拎包入住 随时看房 视野好 " src="https://image1.ljcdn.com/440300-inspection/22fd3df3-2b09-4bd5-95ab-5049275a71c8.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/440300-inspection/22fd3df3-2b09-4bd5-95ab-5049275a71c8.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2215643257428787200.html">
                      现代城华庭 拎包入住 随时看房 视野好                   </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/nanshanzhongxin" target="_blank">南山中心</a>
                  <i> /</i>
                  65㎡
                  <i>/</i> 西                  <i>/</i>
                    2 室 2 厅 1 卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （33 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 6800</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2235689498195533824.html"><img alt="合租 · 深南花园 4室1厅" src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555349930044/0f5d427cc0a414aa1086d2cd7d96fb03.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555349930044/0f5d427cc0a414aa1086d2cd7d96fb03.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2235689498195533824.html">
                    合租・深南花园 4 室 1 厅                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/kejiyuan" target="_blank">科技园</a>
                  <i> /</i>
                  11㎡
                  <i>/</i> 南                  <i>/</i>
                    4 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （34 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  自如                </p>
                                <p class="content__list--item--time oneline">12 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">公寓</i>
                                <i class="content__item__tag--independent_bathroom">独立卫生间</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 3830</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="147665" href="/apartment/17081.html"><img alt=" 宅幸福公寓 坂田华为2号店 品质阳台一居室 " src="https://image1.ljcdn.com/rent-user-avatar/7e3c1738-56ec-4001-929d-cffb456b686e.250x182.jpg" data-src="https://image1.ljcdn.com/rent-user-avatar/7e3c1738-56ec-4001-929d-cffb456b686e.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="147665" href="/apartment/17081.html">
                     宅幸福公寓 坂田华为 2 号店 品质阳台一居室                   </a>
                </p>
                <p class="content__list--item--des">
                                    30㎡
                  <i>/</i> 东南 南 北                  <i>/</i>
                    1 室 1 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  宅幸福公寓                </p>
                                <p class="content__list--item--time oneline">7 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                </p>
                <span class="content__list--item-price"><em> 2400</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2216356313695256576.html"><img alt="  白石洲地铁口 122平米的大三房，另有一个书房。" src="https://image1.ljcdn.com/440300-inspection/db35acbd-db8e-42ce-b024-3db049047b4a.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/440300-inspection/db35acbd-db8e-42ce-b024-3db049047b4a.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2216356313695256576.html">
                      白石洲地铁口 122 平米的大三房，另有一个书房。                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/baishizhou" target="_blank">白石洲</a>
                  <i> /</i>
                  125㎡
                  <i>/</i> 南                  <i>/</i>
                    3 室 2 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （33 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 11000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2222510051493953536.html"><img alt="  世界花园海华居温馨三房，家电齐全拎包入住" src="https://image1.ljcdn.com/440300-inspection/248774a2-d409-41ab-8129-ab3ee0107144.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/440300-inspection/248774a2-d409-41ab-8129-ab3ee0107144.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2222510051493953536.html">
                      世界花园海华居温馨三房，家电齐全拎包入住                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/huaqiaocheng1" target="_blank">华侨城</a>
                  <i> /</i>
                  148㎡
                  <i>/</i> 东南                  <i>/</i>
                    3 室 2 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （23 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 13000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2236249026502860800.html"><img alt="合租 · 星海名城一期六组团 4室1厅" src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555416628207/4841505e03b5eb612755114f1916dd70.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555416628207/4841505e03b5eb612755114f1916dd70.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2236249026502860800.html">
                    合租・星海名城一期六组团 4 室 1 厅                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/qianhai" target="_blank">前海</a>
                  <i> /</i>
                  14㎡
                  <i>/</i> 西                  <i>/</i>
                    4 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （9 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  自如                </p>
                                <p class="content__list--item--time oneline">11 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">公寓</i>
                                <i class="content__item__tag--independent_bathroom">独立卫生间</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 3230</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="147812" href="/apartment/16759.html"><img alt=" 乐乎城市青年社区 平湖店 南向特价单间 开间" src="https://image1.ljcdn.com/rent-user-avatar/5bb75f21-2aa4-490a-83ef-afe914824f7f.250x182.jpg" data-src="https://image1.ljcdn.com/rent-user-avatar/5bb75f21-2aa4-490a-83ef-afe914824f7f.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="147812" href="/apartment/16759.html">
                     乐乎城市青年社区 平湖店 南向特价单间 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                    30㎡
                  <i>/</i> 南                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  乐乎城市青年社区                </p>
                                <p class="content__list--item--time oneline">7 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                </p>
                <span class="content__list--item-price"><em> 1760</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2223221564844023808.html"><img alt="  太古南三房，带空中花园泳池，可拎包入住" src="https://image1.ljcdn.com/440300-inspection/6848f854-19eb-416a-9914-70f9e7616770.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/440300-inspection/6848f854-19eb-416a-9914-70f9e7616770.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2223221564844023808.html">
                      太古南三房，带空中花园泳池，可拎包入住                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/shenzhenwan" target="_blank">深圳湾</a>
                  <i> /</i>
                  89㎡
                  <i>/</i> 东南                  <i>/</i>
                    3 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （30 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">29 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 13000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2224358730525851648.html"><img alt="整租 ·   星河盛世，精装修四房，拎包入住，随时可看！  " src="https://image1.ljcdn.com/440300-inspection/8b2dccab-2127-4ccc-b46f-f23762059cfe.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/440300-inspection/8b2dccab-2127-4ccc-b46f-f23762059cfe.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2224358730525851648.html">
                    整租・星河盛世，精装修四房，拎包入住，随时可看！                    </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/longhuaqu">龙华区</a> - <a href="/zufang/meilinguan" target="_blank">梅林关</a>
                  <i> /</i>
                  134㎡
                  <i>/</i> 南 北                  <i>/</i>
                    4 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （30 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">9 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--decoration">精装</i>
                                <i class="content__item__tag--two_bathroom">双卫生间</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 11000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="145606" href="/apartment/15015.html"><img alt=" 冠寓 深圳景田国际公寓 温馨舒适开间 开间" src="https://image1.ljcdn.com/rent-user-avatar/10a742f0-59b6-421b-9d89-3f8d63b5a38f.250x182.jpg" data-src="https://image1.ljcdn.com/rent-user-avatar/10a742f0-59b6-421b-9d89-3f8d63b5a38f.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="145606" href="/apartment/15015.html">
                     冠寓 深圳景田国际公寓 温馨舒适开间 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                    30㎡
                  <i>/</i> 南 北                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  冠寓                </p>
                                <p class="content__list--item--time oneline">10 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                </p>
                <span class="content__list--item-price"><em> 5300</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2224539732677754880.html"><img alt="花园式小区，三房两卫，南北通透" src="https://image1.ljcdn.com/440300-inspection/72ce2d0b-3338-4a02-831c-c057f2aa31ae.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/440300-inspection/72ce2d0b-3338-4a02-831c-c057f2aa31ae.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2224539732677754880.html">
                    花园式小区，三房两卫，南北通透                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/luohuqu">罗湖区</a> - <a href="/zufang/buxin" target="_blank">布心</a>
                  <i> /</i>
                  81㎡
                  <i>/</i> 北                  <i>/</i>
                    3 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （10 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">27 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 6000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2236304277809405952.html"><img alt="合租 · 康达尔花园五期蝴蝶堡 4室1厅" src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555423212066/2748819b3f08520c61bcfca39a67a091.jpg.250x182.jpg" data-src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555423212066/2748819b3f08520c61bcfca39a67a091.jpg.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2236304277809405952.html">
                    合租・康达尔花园五期蝴蝶堡 4 室 1 厅                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/longgangqu">龙岗区</a> - <a href="/zufang/bujidafen" target="_blank">布吉大芬</a>
                  <i> /</i>
                  17㎡
                  <i>/</i> 南                  <i>/</i>
                    4 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （34 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  自如                </p>
                                <p class="content__list--item--time oneline">11 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">公寓</i>
                                <i class="content__item__tag--independent_bathroom">独立卫生间</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 2590</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="148526" href="/apartment/16359.html"><img alt=" 诚鑫公寓 固戍四店 精致温馨三室一厅 二居+" src="https://image1.ljcdn.com/rent-user-avatar/d87bebef-14bb-4324-add9-b4b0698918f4.250x182.jpg" data-src="https://image1.ljcdn.com/rent-user-avatar/d87bebef-14bb-4324-add9-b4b0698918f4.250x182.jpg" class=" lazyloaded" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="148526" href="/apartment/16359.html">
                     诚鑫公寓 固戍四店 精致温馨三室一厅 二居 +                  </a>
                </p>
                <p class="content__list--item--des">
                                      <span class="room__left">仅剩 1 间</span>
                    <i> /</i>
                                    92㎡
                  <i>/</i> 东                  <i>/</i>
                    3 室 1 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  诚鑫公寓                </p>
                                <p class="content__list--item--time oneline">5 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--bedding_complete">拎包入住</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                </p>
                <span class="content__list--item-price"><em> 4800</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2228958791544872960.html"><img alt="  香蜜湖中旅国际公馆二期 拎包入住 停车方便看小区" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/2cd89ca4-dfb0-4d57-bfe2-c1b28cfb4877.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2228958791544872960.html">
                      香蜜湖中旅国际公馆二期 拎包入住 停车方便看小区                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/futianqu">福田区</a> - <a href="/zufang/xiangmihu" target="_blank">香蜜湖</a>
                  <i> /</i>
                  104㎡
                  <i>/</i> 东                  <i>/</i>
                    3 室 2 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （30 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">21 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 18000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2231706736040091648.html"><img alt="整租 ·   星河标准两房，保养好，初次出租，拎包入住" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/266b7a20-53e6-49a8-83ca-f98453fe0b59.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2231706736040091648.html">
                    整租・星河标准两房，保养好，初次出租，拎包入住                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/longhuaqu">龙华区</a> - <a href="/zufang/meilinguan" target="_blank">梅林关</a>
                  <i> /</i>
                  78㎡
                  <i>/</i> 南                  <i>/</i>
                    2 室 2 厅 1 卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （30 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">17 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--decoration">精装</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 7800</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2236893151505678336.html"><img alt="合租 · 俊峰丽舍 4室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555493416380/41111ea6ff6b596b004512c937a2785f.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2236893151505678336.html">
                    合租・俊峰丽舍 4 室 1 厅                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/xili1" target="_blank">西丽</a>
                  <i> /</i>
                  13㎡
                  <i>/</i> 东                  <i>/</i>
                    4 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （18 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  自如                </p>
                                <p class="content__list--item--time oneline">10 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">公寓</i>
                                <i class="content__item__tag--independent_bathroom">独立卫生间</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 3490</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="148800" href="/apartment/5429.html"><img alt=" 集悦城@红花岭 15栋 30平阳光单房 开间" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-user-avatar/3677e105-e427-4952-af2f-d17d5be29d09.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="148800" href="/apartment/5429.html">
                     集悦城 @红花岭 15 栋 30 平阳光单房 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                      <span class="room__left">仅剩 1 间</span>
                    <i> /</i>
                                    30㎡
                  <i>/</i> 东                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  集悦城 @红花岭                </p>
                                <p class="content__list--item--time oneline">5 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                <i class="content__item__tag--bedding_complete">拎包入住</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_new">新上</i>
                                </p>
                <span class="content__list--item-price"><em> 2505</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2233083520455016448.html"><img alt="  景田北 华盛领寓 精装三房楼龄新 适合居住" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/4da8af98-9367-4ea6-8a83-0bab755888e0.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2233083520455016448.html">
                      景田北 华盛领寓 精装三房楼龄新 适合居住                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/futianqu">福田区</a> - <a href="/zufang/xiangmeibei" target="_blank">香梅北</a>
                  <i> /</i>
                  90㎡
                  <i>/</i> 东                  <i>/</i>
                    3 室 2 厅 1 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （28 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">16 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 7800</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2233253507417513984.html"><img alt="龙联花园 3室2厅 5600元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/ff0c9703-c608-41da-8ca6-0eff3b05dbc7.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2233253507417513984.html">
                    龙联花园 3 室 2 厅 5600 元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/xili1" target="_blank">西丽</a>
                  <i> /</i>
                  94㎡
                  <i>/</i> 南 北                  <i>/</i>
                    3 室 2 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （8 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">15 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 5600</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="117011" href="/apartment/15015.html"><img alt=" 冠寓 深圳景田国际公寓 精致单间 开间" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-user-avatar/18c12652-c0a6-4081-8d1f-d7047b959635.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="117011" href="/apartment/15015.html">
                     冠寓 深圳景田国际公寓 精致单间 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                    28㎡
                  <i>/</i> 北                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  冠寓                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                <i class="content__item__tag--bedding_complete">拎包入住</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                </p>
                <span class="content__list--item-price"><em> 5200-5400</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2239164721976573952.html"><img alt="  太古城南 精装三房 拎包入住 生活便利" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/prod-39d9feab-4655-45c4-bc26-d87f8b606420.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2239164721976573952.html">
                      太古城南 精装三房 拎包入住 生活便利                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/shenzhenwan" target="_blank">深圳湾</a>
                  <i> /</i>
                  89㎡
                  <i>/</i> 西南                  <i>/</i>
                    3 室 2 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （30 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">7 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 12500</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2237394335249203200.html"><img alt="合租 · 碧海名园 5室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555553160197/4f148b13a49e5843b9c04f8473a71821.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2237394335249203200.html">
                    合租・碧海名园 5 室 1 厅                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/baoanqu">宝安区</a> - <a href="/zufang/xixiang" target="_blank">西乡</a>
                  <i> /</i>
                  16㎡
                  <i>/</i> 东南                  <i>/</i>
                    5 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    低楼层                                            （16 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  自如                </p>
                                <p class="content__list--item--time oneline">10 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">公寓</i>
                                <i class="content__item__tag--independent_bathroom">独立卫生间</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 2760</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="148814" href="/apartment/9794.html"><img alt=" 集悦城@红花岭 16栋 18平迷你单房 开间" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-user-avatar/b545a37c-2065-43b6-9ede-848940c2d580.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="148814" href="/apartment/9794.html">
                     集悦城 @红花岭 16 栋 18 平迷你单房 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                      <span class="room__left">仅剩 5 间</span>
                    <i> /</i>
                                    18㎡
                  <i>/</i> 南 西                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  集悦城 @红花岭                </p>
                                <p class="content__list--item--time oneline">5 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                <i class="content__item__tag--bedding_complete">拎包入住</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_new">新上</i>
                                </p>
                <span class="content__list--item-price"><em> 1632-1785</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2241864301357318144.html"><img alt="听泉居 3室2厅 9800元" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/be9b48c4-541a-450b-b71e-5c940a32237b.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2241864301357318144.html">
                    听泉居 3 室 2 厅 9800 元                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/futianqu">福田区</a> - <a href="/zufang/xiangmihu" target="_blank">香蜜湖</a>
                  <i> /</i>
                  91㎡
                  <i>/</i> 南 北                  <i>/</i>
                    3 室 2 厅 1 卫                  <span class="hide">
                    <i>/</i>
                    高楼层                                            （27 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">3 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_new">新上</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 9800</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2202146191997935616.html"><img alt="  香蜜湖温馨三房一厅，家具齐全，拎包入住，期待有缘人" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/bafc210f-4e45-471c-bccf-d5da5e403ad2.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2202146191997935616.html">
                      香蜜湖温馨三房一厅，家具齐全，拎包入住，期待有缘人                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/futianqu">福田区</a> - <a href="/zufang/xiangmihu" target="_blank">香蜜湖</a>
                  <i> /</i>
                  86㎡
                  <i>/</i> 南                  <i>/</i>
                    3 室 1 厅 1 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （28 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 10500</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2237829210880081920.html"><img alt="合租 · 荔林苑 4室1厅" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-house-1/636f69b83827f24f7723a443c68fdbb3-1555605734687/3d4987cc6608537f9accf041792f3e1b.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2237829210880081920.html">
                    合租・荔林苑 4 室 1 厅                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/futianqu">福田区</a> - <a href="/zufang/xiangmihu" target="_blank">香蜜湖</a>
                  <i> /</i>
                  12㎡
                  <i>/</i> 西                  <i>/</i>
                    4 室 1 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （29 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  自如                </p>
                                <p class="content__list--item--time oneline">9 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">公寓</i>
                                <i class="content__item__tag--independent_bathroom">独立卫生间</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 3360</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" data-id="148825" href="/apartment/793.html"><img alt=" 集悦城@红花岭 6栋 18平迷你单间 开间" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/rent-user-avatar/fdb3e596-9132-4ae3-b426-8635d40b3b47.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" data-id="148825" href="/apartment/793.html">
                     集悦城 @红花岭 6 栋 18 平迷你单间 开间                  </a>
                </p>
                <p class="content__list--item--des">
                                      <span class="room__left">仅剩 5 间</span>
                    <i> /</i>
                                    18㎡
                  <i>/</i> 南 西                  <i>/</i>
                    1 室 0 厅 1 卫                </p>
                                <p class="content__list--item--brand oneline">
                  集悦城 @红花岭                </p>
                                <p class="content__list--item--time oneline">5 天前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--authorization_apartment">独栋公寓</i>
                                <i class="content__item__tag--rent_period_month">月租</i>
                                <i class="content__item__tag--bedding_complete">拎包入住</i>
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--deposit_1_pay_1">押一付一</i>
                                <i class="content__item__tag--is_new">新上</i>
                                </p>
                <span class="content__list--item-price"><em> 1680</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2211462529518149632.html"><img alt="       鸿威海怡湾 性 价 比高的大四房 随时可以入住     " src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/4433d0e5-dede-4418-a4a3-f49293157df0.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2211462529518149632.html">
                           鸿威海怡湾 性 价 比高的大四房 随时可以入住                       </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/shenzhenwan" target="_blank">深圳湾</a>
                  <i> /</i>
                  149㎡
                  <i>/</i> 西南                  <i>/</i>
                    4 室 2 厅 2 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （24 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 21000</em> 元 / 月</span>
              </div>
          </div>
                                <div class="content__list--item">
              <a class="content__list--item--aside" target="_blank" href="/zufang/SZ2212063886260584448.html"><img alt="全新装修全新家私、户型方正，客厅出圆弧观景大阳台" src="https://s1.ljcdn.com/matrix_lianjia_pc/dist/pc/src/resource/default/250-182.png?_v=20190426114112aa4" data-src="https://image1.ljcdn.com/440300-inspection/8daac15d-8fdf-48d4-954d-b872e8bfed8b.jpg.250x182.jpg" class="lazyload" data-expand="400"></a>
              <div class="content__list--item--main">
                <p class="content__list--item--title twoline">
                  <a target="_blank" href="/zufang/SZ2212063886260584448.html">
                    全新装修全新家私、户型方正，客厅出圆弧观景大阳台                  </a>
                </p>
                <p class="content__list--item--des">
                  <a target="_blank" href="/zufang/nanshanqu">南山区</a> - <a href="/zufang/hongshuwan" target="_blank">红树湾</a>
                  <i> /</i>
                  234㎡
                  <i>/</i> 东南 南                  <i>/</i>
                    4 室 3 厅 4 卫                  <span class="hide">
                    <i>/</i>
                    中楼层                                            （33 层）
                                      </span>
                </p>
                                <p class="content__list--item--brand oneline">
                  链家                </p>
                                <p class="content__list--item--time oneline">1 个月前发布</p>
                <p class="content__list--item--bottom oneline">
                                <i class="content__item__tag--is_subway_house">近地铁</i>
                                <i class="content__item__tag--is_key">随时看房</i>
                                </p>
                <span class="content__list--item-price"><em> 35000</em> 元 / 月 </span>
              </div>
          </div>
                    </div>"""
soup = BeautifulSoup(html, 'lxml')
list = soup.find_all(attrs={'class': 'content__list--item'})
for div in list:
    temp = div.find_all(attrs={'class': 'content__list--item--title twoline'})
    if temp:
        temp = temp[0].find_all(attrs={'target': '_blank'})
        if temp:
            house = temp[0].text.replace('\n', '').strip()
            zufang_url = temp[0].attrs['href']
        else:
            house = ''
            zufang_url = ''
    else:
        house = ''
        zufang_url = ''
    temp = div.find_all(attrs={'class': 'content__list--item--des'})
    if temp:
        temp = temp[0].text.replace('\n', '').replace(' ', '').split('/')
    else:
        temp = ''
    temp = div.find_all(attrs={'class': 'content__list--item--brand oneline'})
    if temp:
        brand = temp[0].text.strip()
    else:
        temp = ''
    temp = div.find_all(attrs={'class': 'lazyloaded'})
    if temp:
        img_url = temp[0].attrs['data-src']
    else:
        img_url = ''
    temp = div.find_all(attrs={'class': 'content__list--item-price'})
    if temp:
        temp = temp[0].text.replace(' ', '').replace('元/月', '')
        if temp.isdigit():
            price = int(temp)
        else:
            price = temp
    else:
        price = -1
    temp = div.find_all(attrs={'class': 'content__list--item--time oneline'})
    if temp:
        post_time = temp[0].text.replace(' ', '').strip()
    else:
        post_time = ''
    temp = div.find_all(attrs={'class': 'content__list--item--bottom oneline'})
    if temp:
        tag = temp[0].text.split('\n')[1:-1]
    else:
        tag = []
