// Bravaura LLC — site interactions
(function(){
  // landing splash (homepage, first visit of the session only)
  var splash=document.getElementById('site-splash');
  if(splash){
    try{
      if(sessionStorage.getItem('bravaura_splash_seen')){
        splash.remove();
      }else{
        sessionStorage.setItem('bravaura_splash_seen','1');
        var hide=function(){
          splash.classList.add('splash-out');
          setTimeout(function(){splash.remove();},500);
        };
        if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){hide();}
        else{setTimeout(hide,3000);}
      }
    }catch(e){splash.remove();}
  }

  var tog=document.querySelector('.nav-toggle'),links=document.getElementById('nav-links');
  if(tog){tog.addEventListener('click',function(){var o=links.classList.toggle('open');tog.classList.toggle('open',o);tog.setAttribute('aria-expanded',o);});}

  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals=document.querySelectorAll('.reveal');
  if(!reduce && 'IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.14,rootMargin:'0px 0px -8% 0px'});
    reveals.forEach(function(el){io.observe(el);});
  }else{reveals.forEach(function(el){el.classList.add('in');});}

  if(!reduce){
    var blobs=document.querySelectorAll('.hero .blob');
    if(blobs.length){window.addEventListener('scroll',function(){var y=window.scrollY;blobs.forEach(function(b,i){b.style.transform='translateY('+(y*(i?.12:-.08))+'px)';});},{passive:true});}
  }

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function(q){
    q.addEventListener('click',function(){
      var item=q.closest('.faq-item');var a=item.querySelector('.faq-a');
      var open=item.classList.toggle('open');
      q.setAttribute('aria-expanded',open);
      a.style.maxHeight=open?(a.scrollHeight+'px'):'0';
    });
  });

  // current year
  var yr=document.getElementById('year'); if(yr){yr.textContent=new Date().getFullYear();}


  // ---- design menu carousel (arrows + scroll snap)
  document.querySelectorAll('.design-carousel').forEach(function(wrap){
    var track=wrap.querySelector('.design-track');
    var prev=wrap.querySelector('.dcar-prev');
    var next=wrap.querySelector('.dcar-next');
    if(!track||!prev||!next) return;
    function step(){
      var card=track.querySelector('.design-card');
      if(!card) return track.clientWidth*0.8;
      var gap=parseFloat(getComputedStyle(track).columnGap||getComputedStyle(track).gap||22)||22;
      var per=Math.max(1,Math.round(track.clientWidth/(card.offsetWidth+gap)));
      return (card.offsetWidth+gap)*per;
    }
    function sync(){
      var max=track.scrollWidth-track.clientWidth-2;
      prev.disabled = track.scrollLeft<=6;
      next.disabled = track.scrollLeft>=max-6;
    }
    prev.addEventListener('click',function(){track.scrollBy({left:-step(),behavior:'smooth'});});
    next.addEventListener('click',function(){track.scrollBy({left:step(),behavior:'smooth'});});
    track.addEventListener('scroll',function(){window.requestAnimationFrame(sync);});
    window.addEventListener('resize',sync);
    track.addEventListener('keydown',function(e){
      if(e.key==='ArrowRight'){e.preventDefault();track.scrollBy({left:step(),behavior:'smooth'});}
      if(e.key==='ArrowLeft'){e.preventDefault();track.scrollBy({left:-step(),behavior:'smooth'});}
    });
    sync();
  });

  // ---- promo popup (Olipop & Paint). Hides itself from PROMO_END onward.
  (function(){
    var pop=document.getElementById('promo-pop');
    if(!pop) return;
    var PROMO_END=new Date(2026,8,11);           // Sept 11 2026, local time — popup stops showing
    if(new Date()>=PROMO_END){pop.remove();return;}
    try{ if(sessionStorage.getItem('bravaura_promo_olipop')){pop.remove();return;} }catch(e){}
    var card=pop.querySelector('.promo-card');
    var closeBtn=pop.querySelector('.promo-close');
    function close(){
      pop.classList.remove('in');
      try{sessionStorage.setItem('bravaura_promo_olipop','1');}catch(e){}
      setTimeout(function(){pop.classList.remove('on');pop.setAttribute('aria-hidden','true');},300);
      document.removeEventListener('keydown',onKey);
    }
    function onKey(e){ if(e.key==='Escape'){close();} }
    function open(){
      pop.classList.add('on');
      pop.setAttribute('aria-hidden','false');
      requestAnimationFrame(function(){pop.classList.add('in');});
      document.addEventListener('keydown',onKey);
      if(closeBtn) closeBtn.focus();
    }
    closeBtn.addEventListener('click',close);
    var cta=pop.querySelector('.promo-cta');
    if(cta) cta.addEventListener('click',close);
    pop.addEventListener('click',function(e){ if(e.target===pop){close();} });
    // wait out the homepage splash so the two don't collide
    var tries=0;
    (function waitForSplash(){
      var sp=document.getElementById('site-splash');
      if(sp && tries++<80){ setTimeout(waitForSplash,100); return; }
      setTimeout(open,700);
    })();
  })();

  // Forms: graceful AJAX submit with a status message.
  // data-endpoint (the Kit signup band) posts straight to that service;
  // everything else posts to '/' for Netlify Forms.
  document.querySelectorAll('form[data-bravaura-form]').forEach(function(form){
    form.addEventListener('submit',function(ev){
      var status=form.querySelector('.form-status');
      if(!form.checkValidity()){return;} // let native validation handle it
      ev.preventDefault();
      var data=new FormData(form);
      var body=new URLSearchParams();
      data.forEach(function(v,k){body.append(k,v);});
      var endpoint=form.getAttribute('data-endpoint')||'/';
      fetch(endpoint,{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded','Accept':'application/json'},body:body.toString()})
        .then(function(res){
          if(!res.ok){throw new Error('bad status');}
          if(status){status.className='form-status ok';status.textContent=form.getAttribute('data-success')||'Thank you! Your request is in. We\'ll reply by email within 24 hours with your custom quote.';}
          form.reset();
        })
        .catch(function(){
          // If the AJAX call can't get through (local preview, CORS, etc.) but the form
          // posts to a real endpoint, fall back to a plain browser submit so it still works.
          if(form.getAttribute('data-endpoint')){form.submit();return;}
          if(status){status.className='form-status err';status.textContent='Something went wrong sending that. Please email '+ 'bravaurallc@gmail.com' +' or call 908-894-3611 and we\'ll take care of you.';}
        });
    });
  });
})();
