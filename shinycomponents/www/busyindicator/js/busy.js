// Dev version - bave
(()=>{
    var t = {
        564: (t,n,e)=>{
            "use strict";
            e.d(n, {
                Z: ()=>a
            });
            var i = e(81)
              , r = e.n(i)
              , s = e(645)
              , o = e.n(s)()(r());
            o.push([t.id, "\r\n.shinybusy {\r\n  z-index: 9997;\r\n  position: fixed;\r\n}\r\n\r\n.shinybusy-top-right {\r\n  position: fixed;\r\n  top: 10px;\r\n  right: 10px;\r\n}\r\n\r\n.shinybusy-top-left {\r\n  position: fixed;\r\n  top: 10px;\r\n  left: 10px;\r\n}\r\n\r\n.shinybusy-bottom-right {\r\n  position: fixed;\r\n  bottom: 10px;\r\n  right: 10px;\r\n}\r\n\r\n.shinybusy-bottom-left {\r\n  position: fixed;\r\n  bottom: 10px;\r\n  left: 10px;\r\n}\r\n\r\n.shinybusy-full-page {\r\n  margin: auto;\r\n}\r\n\r\n.shinybusy-ready {\r\n  display: none;\r\n}\r\n\r\n.shinybusy-busy {\r\n  display: block;\r\n}\r\n\r\n\r\n.shinybusy-overlay {\r\n  position: fixed;\r\n  width: 100%;\r\n  height: 100%;\r\n  top: 0;\r\n  left: 0;\r\n  right: 0;\r\n  bottom: 0;\r\n  background-color: #FFF; /*rgba(0,0,0,0.4)*/\r\n  z-index: 9900;\r\n}\r\n\r\n.shinybusy-full-page {\r\n  position: fixed;\r\n  top: 50%;\r\n  left: 50%;\r\n  transform: translate(-50%, -50%);\r\n}\r\n\r\n.shinybusy-startup {\r\n  position: fixed;\r\n  width: 100%;\r\n  height: 100%;\r\n  top: 0;\r\n  left: 0;\r\n  right: 0;\r\n  bottom: 0;\r\n  z-index: 9900;\r\n}\r\n\r\n.shinybusy-startup-content {\r\n  position: fixed;\r\n  top: 50%;\r\n  left: 50%;\r\n  transform: translate(-50%, -50%);\r\n  text-align: center;\r\n}\r\n", ""]);
            const a = o
        }
        ,
        645: t=>{
            "use strict";
            t.exports = function(t) {
                var n = [];
                return n.toString = function() {
                    return this.map((function(n) {
                        var e = ""
                          , i = void 0 !== n[5];
                        return n[4] && (e += "@supports (".concat(n[4], ") {")),
                        n[2] && (e += "@media ".concat(n[2], " {")),
                        i && (e += "@layer".concat(n[5].length > 0 ? " ".concat(n[5]) : "", " {")),
                        e += t(n),
                        i && (e += "}"),
                        n[2] && (e += "}"),
                        n[4] && (e += "}"),
                        e
                    }
                    )).join("")
                }
                ,
                n.i = function(t, e, i, r, s) {
                    "string" == typeof t && (t = [[null, t, void 0]]);
                    var o = {};
                    if (i)
                        for (var a = 0; a < this.length; a++) {
                            var c = this[a][0];
                            null != c && (o[c] = !0)
                        }
                    for (var u = 0; u < t.length; u++) {
                        var l = [].concat(t[u]);
                        i && o[l[0]] || (void 0 !== s && (void 0 === l[5] || (l[1] = "@layer".concat(l[5].length > 0 ? " ".concat(l[5]) : "", " {").concat(l[1], "}")),
                        l[5] = s),
                        e && (l[2] ? (l[1] = "@media ".concat(l[2], " {").concat(l[1], "}"),
                        l[2] = e) : l[2] = e),
                        r && (l[4] ? (l[1] = "@supports (".concat(l[4], ") {").concat(l[1], "}"),
                        l[4] = r) : l[4] = "".concat(r)),
                        n.push(l))
                    }
                }
                ,
                n
            }
        }
        ,
        81: t=>{
            "use strict";
            t.exports = function(t) {
                return t[1]
            }
        }
        ,
        882: t=>{
            window,
            t.exports = function(t) {
                var n = {};
                function e(i) {
                    if (n[i])
                        return n[i].exports;
                    var r = n[i] = {
                        i,
                        l: !1,
                        exports: {}
                    };
                    return t[i].call(r.exports, r, r.exports, e),
                    r.l = !0,
                    r.exports
                }
                return e.m = t,
                e.c = n,
                e.d = function(t, n, i) {
                    e.o(t, n) || Object.defineProperty(t, n, {
                        enumerable: !0,
                        get: i
                    })
                }
                ,
                e.r = function(t) {
                    "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(t, Symbol.toStringTag, {
                        value: "Module"
                    }),
                    Object.defineProperty(t, "__esModule", {
                        value: !0
                    })
                }
                ,
                e.t = function(t, n) {
                    if (1 & n && (t = e(t)),
                    8 & n)
                        return t;
                    if (4 & n && "object" == typeof t && t && t.__esModule)
                        return t;
                    var i = Object.create(null);
                    if (e.r(i),
                    Object.defineProperty(i, "default", {
                        enumerable: !0,
                        value: t
                    }),
                    2 & n && "string" != typeof t)
                        for (var r in t)
                            e.d(i, r, function(n) {
                                return t[n]
                            }
                            .bind(null, r));
                    return i
                }
                ,
                e.n = function(t) {
                    var n = t && t.__esModule ? function() {
                        return t.default
                    }
                    : function() {
                        return t
                    }
                    ;
                    return e.d(n, "a", n),
                    n
                }
                ,
                e.o = function(t, n) {
                    return Object.prototype.hasOwnProperty.call(t, n)
                }
                ,
                e.p = "examples",
                e(e.s = 4)
            }([function(t, n, e) {
                var i, r;
                !function(s, o) {
                    "use strict";
                    i = [e(2)],
                    void 0 === (r = function(t) {
                        return function(t, n) {
                            var e = t.jQuery
                              , i = t.console;
                            function r(t, n) {
                                for (var e in n)
                                    t[e] = n[e];
                                return t
                            }
                            var s = Array.prototype.slice;
                            function o(t, n, a) {
                                if (!(this instanceof o))
                                    return new o(t,n,a);
                                var c, u = t;
                                "string" == typeof t && (u = document.querySelectorAll(t)),
                                u ? (this.elements = (c = u,
                                Array.isArray(c) ? c : "object" == typeof c && "number" == typeof c.length ? s.call(c) : [c]),
                                this.options = r({}, this.options),
                                "function" == typeof n ? a = n : r(this.options, n),
                                a && this.on("always", a),
                                this.getImages(),
                                e && (this.jqDeferred = new e.Deferred),
                                setTimeout(this.check.bind(this))) : i.error("Bad element for imagesLoaded " + (u || t))
                            }
                            o.prototype = Object.create(n.prototype),
                            o.prototype.options = {},
                            o.prototype.getImages = function() {
                                this.images = [],
                                this.elements.forEach(this.addElementImages, this)
                            }
                            ,
                            o.prototype.addElementImages = function(t) {
                                "IMG" == t.nodeName && this.addImage(t),
                                !0 === this.options.background && this.addElementBackgroundImages(t);
                                var n = t.nodeType;
                                if (n && a[n]) {
                                    for (var e = t.querySelectorAll("img"), i = 0; i < e.length; i++) {
                                        var r = e[i];
                                        this.addImage(r)
                                    }
                                    if ("string" == typeof this.options.background) {
                                        var s = t.querySelectorAll(this.options.background);
                                        for (i = 0; i < s.length; i++) {
                                            var o = s[i];
                                            this.addElementBackgroundImages(o)
                                        }
                                    }
                                }
                            }
                            ;
                            var a = {
                                1: !0,
                                9: !0,
                                11: !0
                            };
                            function c(t) {
                                this.img = t
                            }
                            function u(t, n) {
                                this.url = t,
                                this.element = n,
                                this.img = new Image
                            }
                            return o.prototype.addElementBackgroundImages = function(t) {
                                var n = getComputedStyle(t);
                                if (n)
                                    for (var e = /url\((['"])?(.*?)\1\)/gi, i = e.exec(n.backgroundImage); null !== i; ) {
                                        var r = i && i[2];
                                        r && this.addBackground(r, t),
                                        i = e.exec(n.backgroundImage)
                                    }
                            }
                            ,
                            o.prototype.addImage = function(t) {
                                var n = new c(t);
                                this.images.push(n)
                            }
                            ,
                            o.prototype.addBackground = function(t, n) {
                                var e = new u(t,n);
                                this.images.push(e)
                            }
                            ,
                            o.prototype.check = function() {
                                var t = this;
                                function n(n, e, i) {
                                    setTimeout((function() {
                                        t.progress(n, e, i)
                                    }
                                    ))
                                }
                                this.progressedCount = 0,
                                this.hasAnyBroken = !1,
                                this.images.length ? this.images.forEach((function(t) {
                                    t.once("progress", n),
                                    t.check()
                                }
                                )) : this.complete()
                            }
                            ,
                            o.prototype.progress = function(t, n, e) {
                                this.progressedCount++,
                                this.hasAnyBroken = this.hasAnyBroken || !t.isLoaded,
                                this.emitEvent("progress", [this, t, n]),
                                this.jqDeferred && this.jqDeferred.notify && this.jqDeferred.notify(this, t),
                                this.progressedCount == this.images.length && this.complete(),
                                this.options.debug && i && i.log("progress: " + e, t, n)
                            }
                            ,
                            o.prototype.complete = function() {
                                var t = this.hasAnyBroken ? "fail" : "done";
                                if (this.isComplete = !0,
                                this.emitEvent(t, [this]),
                                this.emitEvent("always", [this]),
                                this.jqDeferred) {
                                    var n = this.hasAnyBroken ? "reject" : "resolve";
                                    this.jqDeferred[n](this)
                                }
                            }
                            ,
                            c.prototype = Object.create(n.prototype),
                            c.prototype.check = function() {
                                this.getIsImageComplete() ? this.confirm(0 !== this.img.naturalWidth, "naturalWidth") : (this.proxyImage = new Image,
                                this.proxyImage.addEventListener("load", this),
                                this.proxyImage.addEventListener("error", this),
                                this.img.addEventListener("load", this),
                                this.img.addEventListener("error", this),
                                this.proxyImage.src = this.img.src)
                            }
                            ,
                            c.prototype.getIsImageComplete = function() {
                                return this.img.complete && this.img.naturalWidth
                            }
                            ,
                            c.prototype.confirm = function(t, n) {
                                this.isLoaded = t,
                                this.emitEvent("progress", [this, this.img, n])
                            }
                            ,
                            c.prototype.handleEvent = function(t) {
                                var n = "on" + t.type;
                                this[n] && this[n](t)
                            }
                            ,
                            c.prototype.onload = function() {
                                this.confirm(!0, "onload"),
                                this.unbindEvents()
                            }
                            ,
                            c.prototype.onerror = function() {
                                this.confirm(!1, "onerror"),
                                this.unbindEvents()
                            }
                            ,
                            c.prototype.unbindEvents = function() {
                                this.proxyImage.removeEventListener("load", this),
                                this.proxyImage.removeEventListener("error", this),
                                this.img.removeEventListener("load", this),
                                this.img.removeEventListener("error", this)
                            }
                            ,
                            u.prototype = Object.create(c.prototype),
                            u.prototype.check = function() {
                                this.img.addEventListener("load", this),
                                this.img.addEventListener("error", this),
                                this.img.src = this.url,
                                this.getIsImageComplete() && (this.confirm(0 !== this.img.naturalWidth, "naturalWidth"),
                                this.unbindEvents())
                            }
                            ,
                            u.prototype.unbindEvents = function() {
                                this.img.removeEventListener("load", this),
                                this.img.removeEventListener("error", this)
                            }
                            ,
                            u.prototype.confirm = function(t, n) {
                                this.isLoaded = t,
                                this.emitEvent("progress", [this, this.element, n])
                            }
                            ,
                            o.makeJQueryPlugin = function(n) {
                                (n = n || t.jQuery) && ((e = n).fn.imagesLoaded = function(t, n) {
                                    return new o(this,t,n).jqDeferred.promise(e(this))
                                }
                                )
                            }
                            ,
                            o.makeJQueryPlugin(),
                            o
                        }(s, t)
                    }
                    .apply(n, i)) || (t.exports = r)
                }("undefined" != typeof window ? window : this)
            }
            , function(t, n, e) {
                (t.exports = e(3)(!1)).push([t.i, '.ff-container{display:inline-block;position:relative}.ff-container .ff-image{z-index:0;vertical-align:top;opacity:0}.ff-container .ff-canvas{display:inline-block;position:absolute;top:0;left:0;pointer-events:none;z-index:1;vertical-align:top;opacity:0}.ff-container .ff-canvas.ff-canvas-ready{-webkit-transition:opacity 300ms;-o-transition:opacity 300ms;-moz-transition:opacity 300ms;transition:opacity 300ms;opacity:1}.ff-container.ff-active .ff-image{opacity:1}.ff-container.ff-active .ff-canvas.ff-canvas-ready{-webkit-transition:none;-o-transition:none;-moz-transition:none;transition:none;opacity:0}.ff-container.ff-active .ff-overlay{display:none}.ff-container.ff-inactive .ff-canvas.ff-canvas-ready{-webkit-transition:opacity 300ms;-o-transition:opacity 300ms;-moz-transition:opacity 300ms;transition:opacity 300ms;opacity:1}.ff-container.ff-inactive .ff-image{-webkit-transition:opacity 300ms;-o-transition:opacity 300ms;-moz-transition:opacity 300ms;transition:opacity 300ms;-webkit-transition-delay:170ms;-moz-transition-delay:170ms;-o-transition-delay:170ms;transition-delay:170ms;opacity:0}.ff-container.ff-responsive{width:100%}.ff-container.ff-responsive .ff-image,.ff-container.ff-responsive .ff-canvas{width:100%}.ff-container.ff-loading-icon:before{content:"";position:absolute;background-image:url("data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48c3ZnIHdpZHRoPSc1MHB4JyBoZWlnaHQ9JzUwcHgnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDEwMCAxMDAiIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIiBjbGFzcz0idWlsLXNwaW4iPjxyZWN0IHg9IjAiIHk9IjAiIHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiBmaWxsPSJub25lIiBjbGFzcz0iYmsiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg1MCA1MCkiPjxnIHRyYW5zZm9ybT0icm90YXRlKDApIHRyYW5zbGF0ZSgzNCAwKSI+PGNpcmNsZSBjeD0iMCIgY3k9IjAiIHI9IjgiIGZpbGw9IiNmZmZmZmYiPjxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9Im9wYWNpdHkiIGZyb209IjEiIHRvPSIwLjEiIGJlZ2luPSIwcyIgZHVyPSIxcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiPjwvYW5pbWF0ZT48YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InNjYWxlIiBmcm9tPSIxLjUiIHRvPSIxIiBiZWdpbj0iMHMiIGR1cj0iMXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIj48L2FuaW1hdGVUcmFuc2Zvcm0+PC9jaXJjbGU+PC9nPjxnIHRyYW5zZm9ybT0icm90YXRlKDQ1KSB0cmFuc2xhdGUoMzQgMCkiPjxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSI4IiBmaWxsPSIjZmZmZmZmIj48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiBmcm9tPSIxIiB0bz0iMC4xIiBiZWdpbj0iMC4xMnMiIGR1cj0iMXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIj48L2FuaW1hdGU+PGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJzY2FsZSIgZnJvbT0iMS41IiB0bz0iMSIgYmVnaW49IjAuMTJzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlVHJhbnNmb3JtPjwvY2lyY2xlPjwvZz48ZyB0cmFuc2Zvcm09InJvdGF0ZSg5MCkgdHJhbnNsYXRlKDM0IDApIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iOCIgZmlsbD0iI2ZmZmZmZiI+PGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgZnJvbT0iMSIgdG89IjAuMSIgYmVnaW49IjAuMjVzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlPjxhbmltYXRlVHJhbnNmb3JtIGF0dHJpYnV0ZU5hbWU9InRyYW5zZm9ybSIgdHlwZT0ic2NhbGUiIGZyb209IjEuNSIgdG89IjEiIGJlZ2luPSIwLjI1cyIgZHVyPSIxcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiPjwvYW5pbWF0ZVRyYW5zZm9ybT48L2NpcmNsZT48L2c+PGcgdHJhbnNmb3JtPSJyb3RhdGUoMTM1KSB0cmFuc2xhdGUoMzQgMCkiPjxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSI4IiBmaWxsPSIjZmZmZmZmIj48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiBmcm9tPSIxIiB0bz0iMC4xIiBiZWdpbj0iMC4zN3MiIGR1cj0iMXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIj48L2FuaW1hdGU+PGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJzY2FsZSIgZnJvbT0iMS41IiB0bz0iMSIgYmVnaW49IjAuMzdzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlVHJhbnNmb3JtPjwvY2lyY2xlPjwvZz48ZyB0cmFuc2Zvcm09InJvdGF0ZSgxODApIHRyYW5zbGF0ZSgzNCAwKSI+PGNpcmNsZSBjeD0iMCIgY3k9IjAiIHI9IjgiIGZpbGw9IiNmZmZmZmYiPjxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9Im9wYWNpdHkiIGZyb209IjEiIHRvPSIwLjEiIGJlZ2luPSIwLjVzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlPjxhbmltYXRlVHJhbnNmb3JtIGF0dHJpYnV0ZU5hbWU9InRyYW5zZm9ybSIgdHlwZT0ic2NhbGUiIGZyb209IjEuNSIgdG89IjEiIGJlZ2luPSIwLjVzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlVHJhbnNmb3JtPjwvY2lyY2xlPjwvZz48ZyB0cmFuc2Zvcm09InJvdGF0ZSgyMjUpIHRyYW5zbGF0ZSgzNCAwKSI+PGNpcmNsZSBjeD0iMCIgY3k9IjAiIHI9IjgiIGZpbGw9IiNmZmZmZmYiPjxhbmltYXRlIGF0dHJpYnV0ZU5hbWU9Im9wYWNpdHkiIGZyb209IjEiIHRvPSIwLjEiIGJlZ2luPSIwLjYycyIgZHVyPSIxcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiPjwvYW5pbWF0ZT48YW5pbWF0ZVRyYW5zZm9ybSBhdHRyaWJ1dGVOYW1lPSJ0cmFuc2Zvcm0iIHR5cGU9InNjYWxlIiBmcm9tPSIxLjUiIHRvPSIxIiBiZWdpbj0iMC42MnMiIGR1cj0iMXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIj48L2FuaW1hdGVUcmFuc2Zvcm0+PC9jaXJjbGU+PC9nPjxnIHRyYW5zZm9ybT0icm90YXRlKDI3MCkgdHJhbnNsYXRlKDM0IDApIj48Y2lyY2xlIGN4PSIwIiBjeT0iMCIgcj0iOCIgZmlsbD0iI2ZmZmZmZiI+PGFuaW1hdGUgYXR0cmlidXRlTmFtZT0ib3BhY2l0eSIgZnJvbT0iMSIgdG89IjAuMSIgYmVnaW49IjAuNzVzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlPjxhbmltYXRlVHJhbnNmb3JtIGF0dHJpYnV0ZU5hbWU9InRyYW5zZm9ybSIgdHlwZT0ic2NhbGUiIGZyb209IjEuNSIgdG89IjEiIGJlZ2luPSIwLjc1cyIgZHVyPSIxcyIgcmVwZWF0Q291bnQ9ImluZGVmaW5pdGUiPjwvYW5pbWF0ZVRyYW5zZm9ybT48L2NpcmNsZT48L2c+PGcgdHJhbnNmb3JtPSJyb3RhdGUoMzE1KSB0cmFuc2xhdGUoMzQgMCkiPjxjaXJjbGUgY3g9IjAiIGN5PSIwIiByPSI4IiBmaWxsPSIjZmZmZmZmIj48YW5pbWF0ZSBhdHRyaWJ1dGVOYW1lPSJvcGFjaXR5IiBmcm9tPSIxIiB0bz0iMC4xIiBiZWdpbj0iMC44N3MiIGR1cj0iMXMiIHJlcGVhdENvdW50PSJpbmRlZmluaXRlIj48L2FuaW1hdGU+PGFuaW1hdGVUcmFuc2Zvcm0gYXR0cmlidXRlTmFtZT0idHJhbnNmb3JtIiB0eXBlPSJzY2FsZSIgZnJvbT0iMS41IiB0bz0iMSIgYmVnaW49IjAuODdzIiBkdXI9IjFzIiByZXBlYXRDb3VudD0iaW5kZWZpbml0ZSI+PC9hbmltYXRlVHJhbnNmb3JtPjwvY2lyY2xlPjwvZz48L2c+PC9zdmc+");background-position:center center;background-repeat:no-repeat;height:46px;width:46px;z-index:3;top:50%;left:50%;-webkit-transform:translate(-50%, -50%);-moz-transform:translate(-50%, -50%);-ms-transform:translate(-50%, -50%);-o-transform:translate(-50%, -50%);transform:translate(-50%, -50%)}.ff-container .ff-overlay{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF4AAABeCAQAAAAA22vlAAAGFklEQVR42t2ce0yVdRjHP9zlKnfQAwoqV80bImCR90tGhJmShVOxVFJBrdSWVmvmnJlSm2ZbWwunlc4ZOf5IV7NJ84KmFpmZioiKigoKyPWct72vJ4dj0Lm8t9Nz/jt/fd73/L6/5/v8fs9z4H8VTjjhjAuu5o8LLtJ3DoEuYnvghS89pY8PnrjjgrPeH0BEd8fbEHRpaVOZqVUQ2m/cLfomGX+8pAfQ8S8gonvglx/TeEToEKbW69vnD6Annrjp9QEevnU/Q0RDmdAp2m6ffSs0DD964KrHBeSEK96EnlgtdBGN5T9kEYQPHvp7AGc8CCCq7ozQTdzdv2U4AXjrTQEueBFGorFN6DaMzZWFU/t2UIAuwhVfIkkSLIiW6lOLfULx1Y8C3PAnmjTBwmg4UTyFQLzx0MMCcieQAaQLlofp1u73B+sjB7gTRCyjBavCWF+xPs2gvQJE+DjGCFZH8+WjuQRrqwB3gm2DF+P+4Z1jJQVotIDsghcEk7H6q4I4/M02TuUHsBNejPa6c2sTemlhImSAF6Pp/M/ZkgJUNREywYtRe3B7mroKkBFetNFXP5vTXz0bLSu8ZKNr/nhDLRstO7xko39Tx0YrAi/G7e+Vt9GKwYs2uqowK0pJE6EgvKSAG7/nK2ejFYaXbPSpkgxlFKACvKSAfR8Pk18BKsELgrGpcovchaRq8IJUSJ5eIqcCVIWXFHBy/1QC5VGA6vCii7i9d+NQOQpJLeBFBTy4vMl+BWgELyng2q95hNijAA3hJQWUPTpKcbV+AWkMLylgzwdDbFOA9vCiAhovb5zQx3oF6AJeUkDVyQXWHqXoBl5SwLF9k6w5TNQVvHSY+K3lh4l6gxcV0FCxIc1gSSGpQ3hJAZWl2QTghVt3+DqFF3+AMwUE4SXt/w4HL5hatoonoZ5db546hheEq3sQ1767Q8I33yKGYOndOx68IDCE3vg4JLypnWRE2+DqgPC3K0glGn+HhC8pIpUoh3zzd24aZpJEJL4OB3+vNnMlExlEON4OJViTUFqWsJwsUulHID1wdhj4C1XZn7KA6aSTQDg+XRsEncHX3lu323k5c3medAYiXlR7OIQ9aG3bfSjobRaQzWRSiMeAv2SL9W/MjpWnrOd1csggnSH049+rIb37+crq3M/JZw7TGEcScRgsu1XUHL6+cfN3riuYzwwmkkIifSw/iNIUvt1Y/EvkWhbxEs/wJE8QTZg1ByAawp/+a9xHLGY2mYxmGAPoZe31g0bw1TUFX5LPPGmVjyCOCFsufjSAf9C0vcTzTV5lJpNJJZG+hNh26awyvNF08PiA91jEyzzLUwyWtkR/W6/7VYX/81JmIUukVT6GYcTQ275GC9Xga2rX7GQZuUxnAsnEE2l/k5cq8M0tRQd7rmKBtMrTGEQUoXK0VigObxIOnxq8jjxeMSf+/oTL1dioMPzFqllbWcocshhDErGWJn7N4evurxftbS4vMpGRJNBH7lZGheDb2vYcChHtrZj4R0mrPEz+/g9F4MvOjtpgtrdPM5T+9FKmfVd2+Gs3874gn7mP7G3Eo/tuJ123rDQ2bdvvISb+GUyy1t5qCm80HTje710WMYuptthbDeHPVTxK/KPNiV+FMQ0Z4O/Urdn1WOKPIFidARk74Vtbd/0YsPqxxB+iXlexXfBHy0d82CnxezpAO+6V6nnbzYl/rPyJX0H4hsbC4g4VvwKJXyF4o7HkSF87Kn4N4csvTNncqeL30m7swuKBl5q7q3ZQwDxeYLztFb/c8LGM/q/xuuaWogO+K3nNXPEPtL3ilxdeGvK6fr479NLTUi0kVvwPD0HDba/45QzzeN2ObV2BV1zL2dahForRYkvsKsyDjZ7TrvzdGfxe/aa9zuKWqFgtZF+YR0oZH7/w4oWO4O3txaWGd1iobC1kX5iHeUkmwy33k68vXWlvF4S6+p/Kxm0gjxyeU7YWsi/MY9TEkUYGOeSxjBXks4jZZHU6BNXZGLt5gJ1exJLMeDKZwUymk8E4RipfC8mB74EfoUSRyHBSSGUkQ4nX4yrv6u17E0AYEUQRTV8MhDjCnzbgaH+X8Q8RGKy7dFBuqQAAAABJRU5ErkJggg==");background-repeat:no-repeat;max-width:94px;max-height:94px;position:absolute;left:0%;right:0%;top:0%;bottom:0%;margin:auto;-webkit-background-size:contain;-moz-background-size:contain;background-size:contain;background-position:center;pointer-events:none;z-index:100}', ""])
            }
            , function(t, n, e) {
                var i, r;
                "undefined" != typeof window && window,
                void 0 === (r = "function" == typeof (i = function() {
                    "use strict";
                    function t() {}
                    var n = t.prototype;
                    return n.on = function(t, n) {
                        if (t && n) {
                            var e = this._events = this._events || {}
                              , i = e[t] = e[t] || [];
                            return -1 == i.indexOf(n) && i.push(n),
                            this
                        }
                    }
                    ,
                    n.once = function(t, n) {
                        if (t && n) {
                            this.on(t, n);
                            var e = this._onceEvents = this._onceEvents || {};
                            return (e[t] = e[t] || {})[n] = !0,
                            this
                        }
                    }
                    ,
                    n.off = function(t, n) {
                        var e = this._events && this._events[t];
                        if (e && e.length) {
                            var i = e.indexOf(n);
                            return -1 != i && e.splice(i, 1),
                            this
                        }
                    }
                    ,
                    n.emitEvent = function(t, n) {
                        var e = this._events && this._events[t];
                        if (e && e.length) {
                            e = e.slice(0),
                            n = n || [];
                            for (var i = this._onceEvents && this._onceEvents[t], r = 0; r < e.length; r++) {
                                var s = e[r];
                                i && i[s] && (this.off(t, s),
                                delete i[s]),
                                s.apply(this, n)
                            }
                            return this
                        }
                    }
                    ,
                    n.allOff = function() {
                        delete this._events,
                        delete this._onceEvents
                    }
                    ,
                    t
                }
                ) ? i.call(n, e, n, t) : i) || (t.exports = r)
            }
            , function(t, n, e) {
                "use strict";
                t.exports = function(t) {
                    var n = [];
                    return n.toString = function() {
                        return this.map((function(n) {
                            var e = function(t, n) {
                                var e, i = t[1] || "", r = t[3];
                                if (!r)
                                    return i;
                                if (n && "function" == typeof btoa) {
                                    var s = (e = r,
                                    "/*# sourceMappingURL=data:application/json;charset=utf-8;base64," + btoa(unescape(encodeURIComponent(JSON.stringify(e)))) + " */")
                                      , o = r.sources.map((function(t) {
                                        return "/*# sourceURL=" + r.sourceRoot + t + " */"
                                    }
                                    ));
                                    return [i].concat(o).concat([s]).join("\n")
                                }
                                return [i].join("\n")
                            }(n, t);
                            return n[2] ? "@media " + n[2] + "{" + e + "}" : e
                        }
                        )).join("")
                    }
                    ,
                    n.i = function(t, e) {
                        "string" == typeof t && (t = [[null, t, ""]]);
                        for (var i = {}, r = 0; r < this.length; r++) {
                            var s = this[r][0];
                            null != s && (i[s] = !0)
                        }
                        for (r = 0; r < t.length; r++) {
                            var o = t[r];
                            null != o[0] && i[o[0]] || (e && !o[2] ? o[2] = e : e && (o[2] = "(" + o[2] + ") and (" + e + ")"),
                            n.push(o))
                        }
                    }
                    ,
                    n
                }
            }
            , function(t, n, e) {
                "use strict";
                e.r(n);
                var i, r = e(0), s = e.n(r);
                !function(t) {
                    t.START = "start",
                    t.STOP = "stop",
                    t.TOGGLE = "toggle"
                }(i || (i = {}));
                const o = t=>`✨Freezeframe: ${t}✨`
                  , a = (t,...n)=>{
                    console.error(o(t), ...n)
                }
                  , c = t=>"string" == typeof t ? document.querySelectorAll(t) : t
                  , u = (t,n,e)=>{
                    const i = t instanceof Element ? [t] : t;
                    return Array.from(i).reduce(((t,n)=>{
                        if (n instanceof HTMLImageElement)
                            t.push(n),
                            "gif" !== (t=>t.split(".").pop().toLowerCase().substring(0, 3))(n.src) && e.warnings && ((t,...n)=>{
                                console.warn(o(t), ...n)
                            }
                            )("Image does not appear to be a gif", n);
                        else {
                            const e = n.querySelectorAll("img");
                            e.length ? t = t.concat(Array.from(e)) : a("Invalid element", n)
                        }
                        return t
                    }
                    ), [])
                }
                  , l = t=>[...new Set(t)]
                  , d = t=>{
                    const n = window.document.createElement("div");
                    n.innerHTML = t;
                    const e = n.childNodes;
                    return e.length > 1 ? e : e[0]
                }
                ;
                var h, m, f = function() {
                    function t(t, n) {
                        for (var e = 0; e < n.length; e++) {
                            var i = n[e];
                            i.enumerable = i.enumerable || !1,
                            i.configurable = !0,
                            "value"in i && (i.writable = !0),
                            Object.defineProperty(t, i.key, i)
                        }
                    }
                    return function(n, e, i) {
                        return e && t(n.prototype, e),
                        i && t(n, i),
                        n
                    }
                }(), p = (h = ["", ""],
                m = ["", ""],
                Object.freeze(Object.defineProperties(h, {
                    raw: {
                        value: Object.freeze(m)
                    }
                })));
                function y(t, n) {
                    if (!(t instanceof n))
                        throw new TypeError("Cannot call a class as a function")
                }
                var g = function() {
                    function t() {
                        for (var n = this, e = arguments.length, i = Array(e), r = 0; r < e; r++)
                            i[r] = arguments[r];
                        return y(this, t),
                        this.tag = function(t) {
                            for (var e = arguments.length, i = Array(e > 1 ? e - 1 : 0), r = 1; r < e; r++)
                                i[r - 1] = arguments[r];
                            return "function" == typeof t ? n.interimTag.bind(n, t) : "string" == typeof t ? n.transformEndResult(t) : (t = t.map(n.transformString.bind(n)),
                            n.transformEndResult(t.reduce(n.processSubstitutions.bind(n, i))))
                        }
                        ,
                        i.length > 0 && Array.isArray(i[0]) && (i = i[0]),
                        this.transformers = i.map((function(t) {
                            return "function" == typeof t ? t() : t
                        }
                        )),
                        this.tag
                    }
                    return f(t, [{
                        key: "interimTag",
                        value: function(t, n) {
                            for (var e = arguments.length, i = Array(e > 2 ? e - 2 : 0), r = 2; r < e; r++)
                                i[r - 2] = arguments[r];
                            return this.tag(p, t.apply(void 0, [n].concat(i)))
                        }
                    }, {
                        key: "processSubstitutions",
                        value: function(t, n, e) {
                            var i = this.transformSubstitution(t.shift(), n);
                            return "".concat(n, i, e)
                        }
                    }, {
                        key: "transformString",
                        value: function(t) {
                            return this.transformers.reduce((function(t, n) {
                                return n.onString ? n.onString(t) : t
                            }
                            ), t)
                        }
                    }, {
                        key: "transformSubstitution",
                        value: function(t, n) {
                            return this.transformers.reduce((function(t, e) {
                                return e.onSubstitution ? e.onSubstitution(t, n) : t
                            }
                            ), t)
                        }
                    }, {
                        key: "transformEndResult",
                        value: function(t) {
                            return this.transformers.reduce((function(t, n) {
                                return n.onEndResult ? n.onEndResult(t) : t
                            }
                            ), t)
                        }
                    }]),
                    t
                }()
                  , b = function() {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "";
                    return {
                        onEndResult: function(n) {
                            if ("" === t)
                                return n.trim();
                            if ("start" === (t = t.toLowerCase()) || "left" === t)
                                return n.replace(/^\s*/, "");
                            if ("end" === t || "right" === t)
                                return n.replace(/\s*$/, "");
                            throw new Error("Side not supported: " + t)
                        }
                    }
                };
                function v(t) {
                    if (Array.isArray(t)) {
                        for (var n = 0, e = Array(t.length); n < t.length; n++)
                            e[n] = t[n];
                        return e
                    }
                    return Array.from(t)
                }
                var I = function() {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "initial";
                    return {
                        onEndResult: function(n) {
                            if ("initial" === t) {
                                var e = n.match(/^[^\S\n]*(?=\S)/gm)
                                  , i = e && Math.min.apply(Math, v(e.map((function(t) {
                                    return t.length
                                }
                                ))));
                                if (i) {
                                    var r = new RegExp("^.{" + i + "}","gm");
                                    return n.replace(r, "")
                                }
                                return n
                            }
                            if ("all" === t)
                                return n.replace(/^[^\S\n]+/gm, "");
                            throw new Error("Unknown type: " + t)
                        }
                    }
                }
                  , Z = function(t, n) {
                    return {
                        onEndResult: function(e) {
                            if (null == t || null == n)
                                throw new Error("replaceResultTransformer requires at least 2 arguments.");
                            return e.replace(t, n)
                        }
                    }
                }
                  , j = function(t, n) {
                    return {
                        onSubstitution: function(e, i) {
                            if (null == t || null == n)
                                throw new Error("replaceSubstitutionTransformer requires at least 2 arguments.");
                            return null == e ? e : e.toString().replace(t, n)
                        }
                    }
                }
                  , S = {
                    separator: "",
                    conjunction: "",
                    serial: !1
                }
                  , w = function() {
                    var t = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : S;
                    return {
                        onSubstitution: function(n, e) {
                            if (Array.isArray(n)) {
                                var i = n.length
                                  , r = t.separator
                                  , s = t.conjunction
                                  , o = t.serial
                                  , a = e.match(/(\n?[^\S\n]+)$/);
                                if (n = a ? n.join(r + a[1]) : n.join(r + " "),
                                s && i > 1) {
                                    var c = n.lastIndexOf(r);
                                    n = n.slice(0, c) + (o ? r : "") + " " + s + n.slice(c + 1)
                                }
                            }
                            return n
                        }
                    }
                }
                  , x = function(t) {
                    return {
                        onSubstitution: function(n, e) {
                            if (null == t || "string" != typeof t)
                                throw new Error("You need to specify a string character to split by.");
                            return "string" == typeof n && n.includes(t) && (n = n.split(t)),
                            n
                        }
                    }
                }
                  , G = function(t) {
                    return null != t && !Number.isNaN(t) && "boolean" != typeof t
                }
                  , E = (new g(w({
                    separator: ","
                }),I,b),
                new g(w({
                    separator: ",",
                    conjunction: "and"
                }),I,b),
                new g(w({
                    separator: ",",
                    conjunction: "or"
                }),I,b),
                new g(x("\n"),(function() {
                    return {
                        onSubstitution: function(t) {
                            return Array.isArray(t) ? t.filter(G) : G(t) ? t : ""
                        }
                    }
                }
                ),w,I,b));
                new g(x("\n"),w,I,b,j(/&/g, "&amp;"),j(/</g, "&lt;"),j(/>/g, "&gt;"),j(/"/g, "&quot;"),j(/'/g, "&#x27;"),j(/`/g, "&#x60;")),
                new g(Z(/(?:\n(?:\s*))+/g, " "),b),
                new g(Z(/(?:\n\s*)/g, ""),b),
                new g(w({
                    separator: ","
                }),Z(/(?:\s+)/g, " "),b),
                new g(w({
                    separator: ",",
                    conjunction: "or"
                }),Z(/(?:\s+)/g, " "),b),
                new g(w({
                    separator: ",",
                    conjunction: "and"
                }),Z(/(?:\s+)/g, " "),b),
                new g(w,I,b),
                new g(w,Z(/(?:\s+)/g, " "),b),
                new g(I,b),
                new g(I("all"),b);
                const W = ".freezeframe"
                  , P = "ff-loading-icon"
                  , R = "ff-ready"
                  , C = "ff-inactive"
                  , A = "ff-active"
                  , Y = {
                    selector: W,
                    responsive: !0,
                    trigger: "hover",
                    overlay: !1,
                    warnings: !0
                };
                var B, T, L, J = e(1), M = e.n(J), F = function(t, n, e) {
                    if (!n.has(t))
                        throw new TypeError("attempted to set private field on non-instance");
                    return n.set(t, e),
                    e
                }, k = function(t, n) {
                    if (!n.has(t))
                        throw new TypeError("attempted to get private field on non-instance");
                    return n.get(t)
                };
                B = new WeakMap,
                T = new WeakMap,
                L = new WeakMap,
                n.default = class {
                    constructor(t=W, n) {
                        this.items = [],
                        this.$images = [],
                        B.set(this, void 0),
                        T.set(this, void 0),
                        this._eventListeners = Object.assign({}, Object.values(i).reduce(((t,n)=>(t[n] = [],
                        t)), {})),
                        L.set(this, []),
                        "string" == typeof t || t instanceof Element || t instanceof HTMLCollection || t instanceof NodeList ? (this.options = Object.assign(Object.assign({}, Y), n),
                        F(this, B, t)) : "object" != typeof t || n ? a("Invalid Freezeframe.js configuration:", ...[t, n].filter((t=>void 0 !== t))) : (this.options = Object.assign(Object.assign({}, Y), t),
                        F(this, B, this.options.selector)),
                        this._init(k(this, B))
                    }
                    get _stylesInjected() {
                        return !!document.querySelector("style#ff-styles")
                    }
                    _init(t) {
                        this._injectStylesheet(),
                        F(this, T, "ontouchstart"in window || "onmsgesturechange"in window),
                        this._capture(t),
                        this._load(this.$images)
                    }
                    _capture(t) {
                        this.$images = ((...t)=>(...n)=>t.reduceRight(((t,e)=>(...i)=>t(e(...i, ...n))))())(c, u, l)(t, this.options)
                    }
                    _load(t) {
                        s()(t).on("progress", ((t,{img: n})=>{
                            this._setup(n)
                        }
                        ))
                    }
                    _setup(t) {
                        return function(t, n, e, i) {
                            return new (e || (e = Promise))((function(r, s) {
                                function o(t) {
                                    try {
                                        c(i.next(t))
                                    } catch (t) {
                                        s(t)
                                    }
                                }
                                function a(t) {
                                    try {
                                        c(i.throw(t))
                                    } catch (t) {
                                        s(t)
                                    }
                                }
                                function c(t) {
                                    var n;
                                    t.done ? r(t.value) : (n = t.value,
                                    n instanceof e ? n : new e((function(t) {
                                        t(n)
                                    }
                                    ))).then(o, a)
                                }
                                c((i = i.apply(t, n || [])).next())
                            }
                            ))
                        }(this, void 0, void 0, (function*() {
                            const n = this._wrap(t);
                            this.items.push(n),
                            yield this._process(n),
                            this._attach(n)
                        }
                        ))
                    }
                    _wrap(t) {
                        const n = d(E`
    <div class="${"ff-container"} ${P}">
    </div>
  `)
                          , e = d(E`
    <canvas class="${"ff-canvas"}" width="0" height="0">
    </canvas>
  `);
                        var i, r;
                        return this.options.responsive && n.classList.add("ff-responsive"),
                        this.options.overlay && n.appendChild(d(E`
    <div class="${"ff-overlay"}">
    </div>
  `)),
                        t.classList.add("ff-image"),
                        n.appendChild(e),
                        r = n,
                        (i = t).parentNode.insertBefore(r, i),
                        r.appendChild(i),
                        {
                            $container: n,
                            $canvas: e,
                            $image: t
                        }
                    }
                    _process(t) {
                        return new Promise((n=>{
                            const {$canvas: e, $image: i, $container: r} = t
                              , {clientWidth: s, clientHeight: o} = i;
                            e.setAttribute("width", s.toString()),
                            e.setAttribute("height", o.toString()),
                            e.getContext("2d").drawImage(i, 0, 0, s, o),
                            e.classList.add("ff-canvas-ready"),
                            e.addEventListener("transitionend", (()=>{
                                this._ready(r),
                                n(t)
                            }
                            ), {
                                once: !0
                            })
                        }
                        ))
                    }
                    _ready(t) {
                        t.classList.add(R),
                        t.classList.add(C),
                        t.classList.remove(P)
                    }
                    _attach(t) {
                        const {$image: n} = t;
                        if (!k(this, T) && "hover" === this.options.trigger) {
                            const e = ()=>{
                                this._toggleOn(t),
                                this._emit(i.START, t, !0),
                                this._emit(i.TOGGLE, t, !0)
                            }
                              , r = ()=>{
                                this._toggleOff(t),
                                this._emit(i.START, t, !1),
                                this._emit(i.TOGGLE, t, !1)
                            }
                            ;
                            this._addEventListener(n, "mouseleave", r),
                            this._addEventListener(n, "mouseenter", e)
                        }
                        if (k(this, T) || "click" === this.options.trigger) {
                            const e = ()=>{
                                this._toggle(t)
                            }
                            ;
                            this._addEventListener(n, "click", e)
                        }
                    }
                    _addEventListener(t, n, e) {
                        k(this, L).push({
                            $image: t,
                            event: n,
                            listener: e
                        }),
                        t.addEventListener(n, e)
                    }
                    _removeEventListener(t, n, e) {
                        t.removeEventListener(n, e)
                    }
                    _injectStylesheet() {
                        this._stylesInjected || document.head.appendChild(d(E(`\n    <style id="ff-styles">\n      ${M.a.toString()}\n    </style>\n  `)))
                    }
                    _emit(t, n, e) {
                        this._eventListeners[t].forEach((t=>{
                            t(Array.isArray(n) && 1 === n.length ? n[0] : n, e)
                        }
                        ))
                    }
                    _toggleOn(t) {
                        const {$container: n, $image: e} = t;
                        n.classList.contains(R) && (e.setAttribute("src", e.src),
                        n.classList.remove(C),
                        n.classList.add(A))
                    }
                    _toggleOff(t) {
                        const {$container: n} = t;
                        n.classList.contains(R) && (n.classList.add(C),
                        n.classList.remove(A))
                    }
                    _toggle(t) {
                        const {$container: n} = t
                          , e = n.classList.contains(A);
                        return e ? this._toggleOff(t) : this._toggleOn(t),
                        !e
                    }
                    start() {
                        return this.items.forEach((t=>{
                            this._toggleOn(t)
                        }
                        )),
                        this._emit(i.START, this.items, !0),
                        this._emit(i.TOGGLE, this.items, !0),
                        this
                    }
                    stop() {
                        return this.items.forEach((t=>{
                            this._toggleOff(t)
                        }
                        )),
                        this._emit(i.STOP, this.items, !1),
                        this._emit(i.TOGGLE, this.items, !1),
                        this
                    }
                    toggle() {
                        return this.items.forEach((t=>{
                            const n = this._toggle(t);
                            n ? this._emit(i.START, this.items, !1) : this._emit(i.STOP, this.items, !1),
                            this._emit(i.TOGGLE, this.items, n)
                        }
                        )),
                        this
                    }
                    on(t, n) {
                        return this._eventListeners[t].push(n),
                        this
                    }
                    destroy() {
                        k(this, L).forEach((({$image: t, event: n, listener: e})=>{
                            this._removeEventListener(t, n, e)
                        }
                        ))
                    }
                }
            }
            ]).default
        }
        ,
        893: function(t) {
            !function(n) {
                "use strict";
                var e = ".nanobar{width:100%;height:4px;z-index:9999;top:0}.bar{width:0;height:100%;transition:height .3s;background:#000}";
                function i(t, n) {
                    t.classList ? t.classList.add(n) : t.className += " " + n
                }
                t.exports = function(t) {
                    t = t || {};
                    var n, r = document.createElement("div"), s = {
                        el: r,
                        go: function(t) {
                            n(t),
                            100 === t && a()
                        }
                    };
                    function o(t) {
                        r.removeChild(t)
                    }
                    function a() {
                        var t = function(t) {
                            var n = document.createElement("div")
                              , e = 0
                              , r = 0
                              , s = 0
                              , o = {
                                el: n,
                                go: u
                            };
                            function a() {
                                var i = e - r;
                                i < .1 && i > -.1 ? (c(r),
                                s = 0,
                                100 === e && (n.style.height = 0,
                                setTimeout((function() {
                                    t(n)
                                }
                                ), 300))) : (c(e - i / 4),
                                setTimeout(u, 16))
                            }
                            function c(t) {
                                e = t,
                                n.style.width = e + "%"
                            }
                            function u(t) {
                                t >= 0 ? (r = t,
                                s || (s = 1,
                                a())) : s && a()
                            }
                            return i(n, "bar"),
                            o
                        }(o);
                        r.appendChild(t.el),
                        n = t.go
                    }
                    return function() {
                        var t = document.getElementById("nanobarcss");
                        if (null === t) {
                            if ((t = document.createElement("style")).type = "text/css",
                            t.id = "nanobarcss",
                            document.head.insertBefore(t, document.head.firstChild),
                            !t.styleSheet)
                                return t.appendChild(document.createTextNode(e));
                            t.styleSheet.cssText = e
                        }
                    }(),
                    i(r, "nanobar"),
                    t.id && (r.id = t.id),
                    t.classname && i(r, t.classname),
                    t.target ? (r.style.position = "relative",
                    t.target.insertBefore(r, t.target.firstChild)) : (r.style.position = "fixed",
                    document.getElementsByTagName("body")[0].appendChild(r)),
                    a(),
                    s
                }
            }()
        },
        379: t=>{
            "use strict";
            var n = [];
            function e(t) {
                for (var e = -1, i = 0; i < n.length; i++)
                    if (n[i].identifier === t) {
                        e = i;
                        break
                    }
                return e
            }
            function i(t, i) {
                for (var s = {}, o = [], a = 0; a < t.length; a++) {
                    var c = t[a]
                      , u = i.base ? c[0] + i.base : c[0]
                      , l = s[u] || 0
                      , d = "".concat(u, " ").concat(l);
                    s[u] = l + 1;
                    var h = e(d)
                      , m = {
                        css: c[1],
                        media: c[2],
                        sourceMap: c[3],
                        supports: c[4],
                        layer: c[5]
                    };
                    if (-1 !== h)
                        n[h].references++,
                        n[h].updater(m);
                    else {
                        var f = r(m, i);
                        i.byIndex = a,
                        n.splice(a, 0, {
                            identifier: d,
                            updater: f,
                            references: 1
                        })
                    }
                    o.push(d)
                }
                return o
            }
            function r(t, n) {
                var e = n.domAPI(n);
                return e.update(t),
                function(n) {
                    if (n) {
                        if (n.css === t.css && n.media === t.media && n.sourceMap === t.sourceMap && n.supports === t.supports && n.layer === t.layer)
                            return;
                        e.update(t = n)
                    } else
                        e.remove()
                }
            }
            t.exports = function(t, r) {
                var s = i(t = t || [], r = r || {});
                return function(t) {
                    t = t || [];
                    for (var o = 0; o < s.length; o++) {
                        var a = e(s[o]);
                        n[a].references--
                    }
                    for (var c = i(t, r), u = 0; u < s.length; u++) {
                        var l = e(s[u]);
                        0 === n[l].references && (n[l].updater(),
                        n.splice(l, 1))
                    }
                    s = c
                }
            }
        }
        ,
        569: t=>{
            "use strict";
            var n = {};
            t.exports = function(t, e) {
                var i = function(t) {
                    if (void 0 === n[t]) {
                        var e = document.querySelector(t);
                        if (window.HTMLIFrameElement && e instanceof window.HTMLIFrameElement)
                            try {
                                e = e.contentDocument.head
                            } catch (t) {
                                e = null
                            }
                        n[t] = e
                    }
                    return n[t]
                }(t);
                if (!i)
                    throw new Error("Couldn't find a style target. This probably means that the value for the 'insert' parameter is invalid.");
                i.appendChild(e)
            }
        }
        ,
        216: t=>{
            "use strict";
            t.exports = function(t) {
                var n = document.createElement("style");
                return t.setAttributes(n, t.attributes),
                t.insert(n, t.options),
                n
            }
        }
        ,
        565: (t,n,e)=>{
            "use strict";
            t.exports = function(t) {
                var n = e.nc;
                n && t.setAttribute("nonce", n)
            }
        }
        ,
        795: t=>{
            "use strict";
            t.exports = function(t) {
                var n = t.insertStyleElement(t);
                return {
                    update: function(e) {
                        !function(t, n, e) {
                            var i = "";
                            e.supports && (i += "@supports (".concat(e.supports, ") {")),
                            e.media && (i += "@media ".concat(e.media, " {"));
                            var r = void 0 !== e.layer;
                            r && (i += "@layer".concat(e.layer.length > 0 ? " ".concat(e.layer) : "", " {")),
                            i += e.css,
                            r && (i += "}"),
                            e.media && (i += "}"),
                            e.supports && (i += "}");
                            var s = e.sourceMap;
                            s && "undefined" != typeof btoa && (i += "\n/*# sourceMappingURL=data:application/json;base64,".concat(btoa(unescape(encodeURIComponent(JSON.stringify(s)))), " */")),
                            n.styleTagTransform(i, t, n.options)
                        }(n, t, e)
                    },
                    remove: function() {
                        !function(t) {
                            if (null === t.parentNode)
                                return !1;
                            t.parentNode.removeChild(t)
                        }(n)
                    }
                }
            }
        }
        ,
        589: t=>{
            "use strict";
            t.exports = function(t, n) {
                if (n.styleSheet)
                    n.styleSheet.cssText = t;
                else {
                    for (; n.firstChild; )
                        n.removeChild(n.firstChild);
                    n.appendChild(document.createTextNode(t))
                }
            }
        }
    }
      , n = {};
    function e(i) {
        var r = n[i];
        if (void 0 !== r)
            return r.exports;
        var s = n[i] = {
            id: i,
            exports: {}
        };
        return t[i].call(s.exports, s, s.exports, e),
        s.exports
    }
    e.n = t=>{
        var n = t && t.__esModule ? ()=>t.default : ()=>t;
        return e.d(n, {
            a: n
        }),
        n
    }
    ,
    e.d = (t,n)=>{
        for (var i in n)
            e.o(n, i) && !e.o(t, i) && Object.defineProperty(t, i, {
                enumerable: !0,
                get: n[i]
            })
    }
    ,
    e.o = (t,n)=>Object.prototype.hasOwnProperty.call(t, n),
    (()=>{
        "use strict";
        const t = jQuery;
        var n = e.n(t);
        Shiny;
        var i = e(882)
          , r = e.n(i)
          , s = e(893)
          , o = e.n(s)
          , a = e(379)
          , c = e.n(a)
          , u = e(795)
          , l = e.n(u)
          , d = e(569)
          , h = e.n(d)
          , m = e(565)
          , f = e.n(m)
          , p = e(216)
          , y = e.n(p)
          , g = e(589)
          , b = e.n(g)
          , v = e(564)
          , I = {};
        I.styleTagTransform = b(),
        I.setAttributes = f(),
        I.insert = h().bind(null, "head"),
        I.domAPI = l(),
        I.insertStyleElement = y(),
        c()(v.Z, I),
        v.Z && v.Z.locals && v.Z.locals,
        window.NodeList && !NodeList.prototype.forEach && (NodeList.prototype.forEach = function(t, n) {
            n = n || window;
            for (var e = 0; e < this.length; e++)
                t.call(n, this[e], e, this)
        }
        ),
        n()((function() {
            document.querySelectorAll('script[data-for="shinybusy"]').forEach((function(t) {
                var e, i, s, a, c, u, l, d = "", h = JSON.parse(t.innerHTML);
                if (h && (e = h.id,
                a = h.timeout,
                c = h.mode,
                u = h.position,
                l = h.classname,
                h.hasOwnProperty("type") && (d = h.type)),
                "spin" == c && ("auto" == d && (n()(document).on("shiny:busy", (function(t) {
                    i = setTimeout((function() {
                        n()("#" + e).removeClass("shinybusy-ready"),
                        n()("#" + e).addClass("shinybusy-busy"),
                        "full-page" == u && (n()("#" + e + "_overlay").removeClass("shinybusy-ready"),
                        n()("#" + e + "_overlay").addClass("shinybusy-busy"))
                    }
                    ), a)
                }
                )),
                n()(document).on("shiny:idle", (function(t) {
                    clearTimeout(i),
                    n()("#" + e).removeClass("shinybusy-busy"),
                    n()("#" + e).addClass("shinybusy-ready"),
                    "full-page" == u && (n()("#" + e + "_overlay").removeClass("shinybusy-busy"),
                    n()("#" + e + "_overlay").addClass("shinybusy-ready"))
                }
                ))),
                "start" == d && n()(document).on("shiny:idle", (function(t) {
                    n()(".shinybusy").removeClass("shinybusy-busy"),
                    n()(".shinybusy").addClass("shinybusy-ready")
                }
                ))),
                "gif" == c)
                    if ("full-page" != u) {
                        var m = new (r())(".shinybusy-freezeframe");
                        "auto" == d ? (n()(document).on("shiny:busy", (function(t) {
                            "full-page" == u && (n()(".shinybusy").removeClass("shinybusy-ready"),
                            n()(".shinybusy").addClass("shinybusy-busy")),
                            i = setTimeout((function() {
                                m.start()
                            }
                            ), a)
                        }
                        )),
                        n()(document).on("shiny:idle", (function(t) {
                            "full-page" == u && (n()(".shinybusy").removeClass("shinybusy-busy"),
                            n()(".shinybusy").addClass("shinybusy-ready")),
                            clearTimeout(i),
                            m.stop()
                        }
                        ))) : (Shiny.addCustomMessageHandler("shinybusy-play-gif", (function(t) {
                            m.start()
                        }
                        )),
                        Shiny.addCustomMessageHandler("shinybusy-stop-gif", (function(t) {
                            m.stop()
                        }
                        )))
                    } else
                        n()(document).on("shiny:busy", (function(t) {
                            i = setTimeout((function() {
                                n()(".shinybusy").removeClass("shinybusy-ready"),
                                n()(".shinybusy").addClass("shinybusy-busy")
                            }
                            ), a)
                        }
                        )),
                        n()(document).on("shiny:idle", (function(t) {
                            clearTimeout(i),
                            n()(".shinybusy").removeClass("shinybusy-busy"),
                            n()(".shinybusy").addClass("shinybusy-ready")
                        }
                        ));
                if ("nanobar" == c) {
                    var f = new (o())({
                        classname: l
                    });
                    var intvs = []
                    "manual" == d && Shiny.addCustomMessageHandler("shinybusy-update-nanobar", (function(t) {
                        f.go(t.value)
                    }
                    )),
                    "auto" == d && (n()(document).on("shiny:busy", (function(t) {
                        s = setInterval((function() {
                            f.go(100)
                        }
                        ), a);
                        intvs.push(s)
                    }
                    )),
                    n()(document).on("shiny:idle", (function(t) {
                        clearInterval(s)
                        console.log("intervals " + intvs.length)
                        while (intvs.length) {
                            i = intvs.pop()
                            clearInterval(i)
                        }
                    }
                    )))
                }
            }
            )),
            Shiny.addCustomMessageHandler("shinybusy-show-spinner", (function(t) {
                t.hasOwnProperty("spin_id") ? (n()("#" + t.spin_id).removeClass("shinybusy-ready"),
                n()("#" + t.spin_id).addClass("shinybusy-busy")) : (n()(".shinybusy").removeClass("shinybusy-ready"),
                n()(".shinybusy").addClass("shinybusy-busy"))
            }
            )),
            Shiny.addCustomMessageHandler("shinybusy-hide-spinner", (function(t) {
                t.hasOwnProperty("spin_id") ? (n()("#" + t.spin_id).removeClass("shinybusy-busy"),
                n()("#" + t.spin_id).addClass("shinybusy-ready")) : (n()(".shinybusy").removeClass("shinybusy-busy"),
                n()(".shinybusy").addClass("shinybusy-ready"))
            }
            ))
        }
        ))
    }
    )()
}
)();
