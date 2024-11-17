<form method="post" action="/submit/">
    {% csrf_token %}
    <input type="text" name="example_field">
    <button type="submit">Submit</button>
</form>
