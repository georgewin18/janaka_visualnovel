screen credit_scr:
    key "K_RETURN" action Hide("none")
    key "K_KP_ENTER" action Hide("none")
    key "K_SPACE" action Hide("none")
    
    key "mousedown_4" action Hide("none")
    key "K_PAGEUP" action Hide("none")
    key "mousedown_5" action Hide("none")
    key "K_PAGEDOWN" action Hide("none")
    
    key "mouseup_3" action Hide("none")
    key "mouseup_1" action Hide("none")

    key "K_ESCAPE" action Return("none")

label credit:
    scene black
    with dissolve

    $ quick_menu = False
    centered "{i}Disinilah cerita kalian dimulai...{/i}"

    show bg end with dissolve
    with Pause(2)
    
    show screen credit_scr
    $ renpy.movie_cutscene("images/credits/jnp_credits.webm", stop_music=False)

    scene black
    with Pause(2)

    $ quick_menu = True
    hide screen  credit_scr

    return