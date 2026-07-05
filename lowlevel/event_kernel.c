void event_loop() {

    while (1) {

        EVENT e = read_event_stream();

        ANALYSIS a = analyze_event(e);

        if (a.risk > 0.8) {
            execute_containment();
        }

        update_learning_model();

        evolve_system_state();
    }
}
