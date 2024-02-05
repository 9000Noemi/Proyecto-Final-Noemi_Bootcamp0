
'''
<form action="/purchase" method="post">
  <label for="moneda_from">Moneda de origen:</label>
  <input type="text" id="moneda_from" name="moneda_from" required>

  <label for="moneda_to">Moneda de destino:</label>
  <input type="text" id="moneda_to" name="moneda_to" required>

  <label for="cantidad_from">Cantidad:</label>
  <input type="number" id="cantidad_from" name="cantidad_from" required>

  <label for="cantidad_to">Tipo de cambio:</label>
  <input type="text" id="cantidad_to" name="cantidad_to"  value="{{dataForm['rate']}}" readonly>
  
  <button class="material-symbols-outlined" id="cantidad_to" name="cantidad_to" onclick="{{tipoCambio}}">Calcular
  </button>

  <label for="total">Total de inversión:</label>
  <input type="text" id="total" name="total" readonly>

  <button type="button" onclick="{{totalCantidad}}">Calcular</button>
</form>
  <span>{{dataForm}}</span>


  <!--INSERTAMOS LOS ICONOS CALCULATE Y CHECK QUE AHORA ESTAN EN BASE--> 

  <a href="#">
  <span class="material-symbols-outlined">
    check_box
    </span>
  </a>

    <a href="#">
      <span class="material-symbols-outlined">
        calculate
        </span>
    </a>

'''

'''
  <!--<<div class="grid">
  </div>
    <label for="FROM">FROM</label>
    <select id="from" required>
      <option value="" selected>Select a coin…</option>
      <option>EUR</option>
      <option>BTC</option>
      <option>ETH</option>
      <option>USDT</option>
      <option>BNB</option>
      <option>XRP</option>
      <option>ADA</option>
      <option>SOL</option>
      <option>DOT</option>
      <option>MATIC</option>
     
    </select>
  </div>
   
    <label for="TO">TO</label>
    <select id="TO" required>
      <option value="" selected>Select a coin…</option>
      <option>EUR</option>
      <option>BTC</option>
      <option>ETH</option>
      <option>USDT</option>
      <option>BNB</option>
      <option>XRP</option>
      <option>ADA</option>
      <option>SOL</option>
      <option>DOT</option>
      <option>MATIC</option>
     
    </select>

  </div>

  <label for="Q">QUANTITY</label>
  <input type="q" id=q" name="q"  required>
  
  <button type="calculate">CALCULATE</button>

  <label for="cantidad_to">Tipo de cambio:</label>
  <input type="text" id="cantidad_to" name="cantidad_to"  value="{{dataForm['rate']}}" readonly>
 
  <label for="P.U">P.U</label>
  <input type="p.u" id=p.u" name="p.u"  required>
 
  <button type="execute">EXECUTE</button>>-->
  '''

'''               
<li {% if active_page == 'listaMovimientos' %}class= "active"{% endif %}><a href="/" role="button">Inicio</a></li>
<li {% if active_page == 'registroMovimientos' %}class= "active"{% endif %}><a href="/purchase" role="button">Compra</a></li>
<li {% if active_page == 'estadoInversion' %}class= "active"{% endif %}><a href="/status" role="button">Status</a></li>
'''
                