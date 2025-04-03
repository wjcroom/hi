// ==UserScript==
// @name         模拟点击特定页面li中的a元素
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  在https://learn.ourteacher.com.cn页面从第5个li开始，模拟点击其中的a元素，间隔5分钟
// @author       You
// @match        https://learn.ourteacher.com.cn/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // 使用 :gt(4) 选择器从第 5 个 li 元素开始获取所有 li 元素
    var allLiElements = $('li:gt(4)');
    var delay = 0;
    allLiElements.each(function (index) {
        var aElement = $(this).find('a');
        if (aElement.length > 0) {
            setTimeout(function () {
                aElement.trigger('click');
                console.log('模拟点击了第'+ (index + 5 + 1) +'个 li 中的 a 元素');
            }, delay);
            delay += 300000;
        }
    });
})();
