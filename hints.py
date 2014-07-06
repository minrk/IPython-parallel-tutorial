from IPython.display import display, HTML

def mmhint():
    display(HTML("""
<button onclick="$('#mmhint1').toggle();">hint 1</button>
<div id="mmhint1">
Remember - multiply rows of one by the columns of the other.
</div>

<br/>
<button onclick="$('#mmhint').toggle();">hint 2</button>
<div id="mmhint">
easiest implementation involves one each of: push, scatter, execute, gather
</div>
<script type="text/javascript">
    $('#mmhint').hide();
    $('#mmhint1').hide();
</script>
"""))

def nesthint():
    display(HTML("""
<button onclick="$('#hint').toggle();" label="hint">
hint
</button>

<div id="hint">
`itertools.product` and `zip` will be helpful.
</div>
<script type="text/javascript">
    $('#hint').hide();
</script>
    """))