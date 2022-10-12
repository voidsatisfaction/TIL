## Sources

- [How to css parallax](https://www.w3schools.com/howto/howto_css_parallax.asp)
- [W3School](https://www.w3schools.com/howto/tryhow_css_parallax_demo.htm)

## Code

```html

<style>
.parallax { 
    /* The image used */
    background-image: url("img_parallax.jpg");

    /* Set a specific height */
    height: 500px; 

    /* Create the parallax scrolling effect */
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
</style>

```